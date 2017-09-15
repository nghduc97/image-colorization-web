from flask import Blueprint, request, abort
from utils import mongo, Logger, make_token, parse_token, check_has_fields, check_field_length
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util

user_blueprint = Blueprint('user', __name__, url_prefix='/api/user')

@user_blueprint.route('/', methods=['GET'])
def user_info():
    if 'Authorization' not in request.headers:
        abort(401, 'not_logged_in')
    
    auth_data = parse_token(request.headers['Authorization'])
    user_id = auth_data['user_id']
    user = mongo['users'].find_one(user_id, { '_id': 0, 'display_name': 1, 'authority': 1})
    return json_util.dumps(user)

@user_blueprint.route('/login', methods=['POST'])
def login():
    if 'Authorization' in request.headers:
        abort(400, 'already_logged_in')

    data = request.json
    check_has_fields(data, ['username', 'password'])

    user = mongo['users'].find_one({ 'username': data['username'] })
    if check_password_hash(user['hashed_password'], data['password']):
        return make_token({ 'user_id': user['_id'] })
    
    abort(400, 'invalid_password_or_username')

@user_blueprint.route('/register', methods=['POST'])
def register():
    # validation
    data = request.json
    check_has_fields(data, ['username', 'password', 'display_name'])

    # no length limit for development
    # check_field_length(data, 'username', 6, 32)
    # check_field_length(data, 'password', 6, 32)

    user = mongo['users'].find_one({ 'username': data['username'] })
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
    
    # return authentication token
    return make_token({ 'user_id': result.inserted_id })
