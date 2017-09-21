''' /api/user routes controller '''

from flask import Blueprint, request, abort, current_app
from bson import json_util
from werkzeug.security import generate_password_hash, check_password_hash
from server.utils.mongo import mongo
from server.utils.request_validator import check_has_fields
from server.utils.response import ejson_response
from server.utils.token_parser import make_token, parse_token


user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')


USER_INFO_INCLUDE = {
    '_id': 0,
    'username': 1,
    'display_name': 1,
    'authority': 1
}


@user_blueprint.route('/', methods=['GET'])
def verify_user():
    check_has_fields(request.headers, ['Authorization'])

    token = request.headers['Authorization']
    username = parse_token(token)
    user_info = _get_user_info_by_username(username)
    if user_info is None:
        abort(400, 'invalid_token')

    return ejson_response({
        'token': make_token(username),
        'user_info': user_info
    })


@user_blueprint.route('/login', methods=['POST'])
def login():
    if 'Authorization' in request.headers:
        abort(400, 'already_logged_in')

    # get and validate data
    data = json_util.loads(request.data)
    check_has_fields(data, ['username', 'password'])

    # check for correct username & password
    user = mongo['users'].find_one({
        'username': data['username']
    }, {
        'hashed_password': 1
    })
    if user is not None \
        and check_password_hash(user['hashed_password'], data['password']):

        user_info = _get_user_info_by_id(user['_id'])
        current_app.logger.info('user login, id: ' + str(user['_id']))

        # return token and user-infos
        return ejson_response({
            'token': make_token(data['username']),
            'user_info': user_info
        })

    abort(400, 'invalid_password_or_username')


@user_blueprint.route('/register', methods=['POST'])
def register():
    # validation
    data = request.json
    check_has_fields(data, ['username', 'password', 'display_name'])

    # no length limit for development
    # check_field_length(data, 'username', 6, 32)
    # check_field_length(data, 'password', 6, 32)

    user = _get_user_info_by_username(data['username'])
    if user is not None:
        abort(400, 'username already taken')

    # create user
    hashed_password = generate_password_hash(data['password'], salt_length=30)
    result = mongo['users'].insert_one({
        'username': data['username'],
        'hashed_password': hashed_password,
        'display_name': data['display_name'],
        'authority': 4
    })

    if not result.acknowledged:
        abort(500, 'fail_to_write_to_database')

    current_app.logger.info('user register, id: ' + str(result.inserted_id))

    # return authentication token and user info
    user_info = _get_user_info_by_id(result.inserted_id)
    return ejson_response({
        'token': make_token(user_info['username']),
        'user_info': user_info
    })


def _get_user_info_by_id(user_id):
    return mongo['users'].find_one(user_id, USER_INFO_INCLUDE)


def _get_user_info_by_username(username):
    return mongo['users'].find_one({'username': username}, USER_INFO_INCLUDE)
