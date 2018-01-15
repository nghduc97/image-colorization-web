''' /api/user routes controller '''

from datetime import timedelta
import flask
import flask_jwt_extended as jwt
import werkzeug.security as security
import database.queries as db


user_blueprint = flask.Blueprint('user', __name__, url_prefix='/api/user')


@user_blueprint.route('/', methods=['GET'])
@jwt.jwt_required
def get_user_info():
    user_id = jwt.get_jwt_identity()
    user = db.query_fetchone('get_user_by_id', {'id': user_id})
    return _create_user_response(user)


@user_blueprint.route('/login', methods=['POST'])
def login():
    body = flask.request.get_json()
    username = body['username']
    password = body['password']

    user = db.query_fetchone('get_user_by_username', {'username': username})
    if security.check_password_hash(user['hashed_password'], password):
        return _create_user_response(user)

    flask.abort(400, 'incorrect username or password')


@user_blueprint.route('/register', methods=['POST'])
def register():
    body = flask.request.get_json()
    username = body['username']
    password = body['password']
    display_name = body['display_name']

    user = db.query_fetchone('insert_user', {
        'username': username,
        'hashed_password': security.generate_password_hash(password, salt_length=32),
        'display_name': display_name,
        'authority': 4,
    })

    return _create_user_response(user)


@user_blueprint.route('/info-change', methods=['POST'])
@jwt.jwt_required
def info_change():
    body = flask.request.get_json()
    display_name = body['display_name']
    old_password = body['old_password']
    new_password = body['new_password']

    user_id = jwt.get_jwt_identity()
    user = db.query_fetchone('get_user_by_id', {'id': user_id})
    if not security.check_password_hash(user['hashed_password'], old_password):
        flask.abort(401)

    hash_password = user['hashed_password']
    if new_password:
        hash_password = security.generate_password_hash(new_password, salt_length=32)

    user = db.query_fetchone('update_user_info', {
        'display_name': display_name,
        'hashed_password': hash_password,
    })
    return _create_user_response(user)


def _create_user_response(user):
    return flask.jsonify({
        'token': jwt.create_access_token(
            identity=user['id'],
            expires_delta=timedelta(days=1),
        ),
        'user_info': {
            'display_name': user['display_name'],
            'authority': user['authority'],
        },
    })
