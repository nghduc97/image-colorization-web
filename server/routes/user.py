''' /api/user routes controller '''

import flask
from database.queries import do_query


user_blueprint = flask.Blueprint('user', __name__, url_prefix='/api/user')


@user_blueprint.route('/', methods=['GET'])
def verify_user():
    return flask.jsonify(list(do_query('get_post_by_id', {'id': 1})))
    return flask.jsonify({
        'token': '',
        'user_info': ''
    })


@user_blueprint.route('/login', methods=['POST'])
def login():
    pass


@user_blueprint.route('/register', methods=['POST'])
def register():
    pass
