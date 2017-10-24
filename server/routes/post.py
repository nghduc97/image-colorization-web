''' /api/post routes controller '''

from datetime import datetime
import flask
import flask_jwt_extended as jwt
import database.queries as db


post_blueprint = flask.Blueprint("post", __name__, url_prefix="/api/post")


@post_blueprint.route('/top', methods=["GET"])
def get_top_posts():
    order_by = flask.request.args.get('sortby', 'time')
    post_type = int(flask.request.args.get('type', 1))
    offset = int(flask.request.args.get('offset', 0))
    limit = int(flask.request.args.get('limit', 5))

    post_type_name = ''
    if post_type == 1:
        post_type_name = 'image'
    elif post_type == 2:
        post_type_name = 'discuss'
    else:
        flask.abort(400, 'Invalid "type" argument, value="{}"'.format(post_type))

    query = 'get_{0}_posts_order_by_{1}'.format(post_type_name, order_by)
    posts = db.query_fetchall(query, {
        'offset': offset,
        'limit': limit,
    })
    return flask.jsonify(posts)


@post_blueprint.route('/comments', methods=['GET'])
def get_comments_on_post():
    post_id = int(flask.request.args.get('post_id'))
    comments = db.query_fetchall('get_comments_by_post', {'post_id': post_id})
    return flask.jsonify(comments)


@post_blueprint.route('/clap', methods=['PUT'])
@jwt.jwt_required
def clap_on_post():
    body = flask.request.get_json()
    user_id = jwt.get_jwt_identity()
    post_id = int(body['post_id'])
    amount = int(body['amount'])

    result = db.query_fetchone('upsert_clap', {
        'user_id': user_id,
        'post_id': post_id,
        'amount': amount,
    })
    return flask.jsonify(result)


@post_blueprint.route('/comment', methods=['POST'])
@jwt.jwt_required
def comment_on_post():
    body = flask.request.get_json()
    user_id = jwt.get_jwt_identity()
    post_id = int(body['post_id'])
    content = body['content']
    time = datetime.utcnow()

    result = db.query_fetchone('insert_comment', {
        'user_id': user_id,
        'post_id': post_id,
        'content': content,
        'time': time,
    })
    return flask.jsonify(result)
