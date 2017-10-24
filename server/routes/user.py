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
    security.check_password_hash(user['hashed_password'], password)
    return _create_user_response(user)


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
