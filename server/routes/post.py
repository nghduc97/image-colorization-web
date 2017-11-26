''' /api/post routes controller '''

from datetime import datetime
import flask
import flask_jwt_extended as jwt
import database.queries as db
import utils.file as file


post_blueprint = flask.Blueprint("post", __name__, url_prefix="/api/post")


@post_blueprint.route('/', methods=['POST'])
@jwt.jwt_required
def create_post():
    body = flask.request.get_json()

    query = ''
    params = {
        'hidden': False,
        'time': datetime.utcnow(),
        'uploader_id': jwt.get_jwt_identity(),
        'title': body['title'],
        'total_claps': 0,
    }

    if body['type'] == 1:
        params['status'] = 'queue'
        query = 'insert_image_post'
    else:
        params['content'] = body['content']
        query = 'insert_discuss_post'

    data = db.query_fetchone(query, params)
    if body['type'] == 1:
        file.write_base64_image_to_file(str(data['post_id']), body['file_b64'])

    return flask.jsonify(data)


@post_blueprint.route('/top', methods=['GET'])
def get_top_posts():
    order_by = flask.request.args.get('sortby', 'time')
    post_type = int(flask.request.args.get('type', 1))
    offset = int(flask.request.args.get('offset', 0))
    limit = int(flask.request.args.get('limit', 5))

    if post_type not in [1, 2]:
        flask.abort(400, 'Invalid "type" argument, value="{}"'.format(post_type))

    query = 'get_posts_order_by_{}'.format(order_by)
    posts = db.query_fetchall(query, {
        'type': post_type,
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


@post_blueprint.route('/set-tag', methods=['POST'])
@jwt.jwt_required
def set_tag_of_post():
    body = flask.request.get_json()
    user_id = jwt.get_jwt_identity()
    post_id = int(body['post_id'])
    tags = [{'post_id': post_id, 'tag': tag_name} for tag_name in body['tags']]

    # check if is owner or moderator and above
    post = db.query_fetchone('get_post_by_id', {'id': post_id})
    user = db.query_fetchone('get_user_by_id', {'id': user_id})
    if user_id != post['uploader_id'] and user['authority'] > 2:
        flask.abort(401)

    # delete all created post_tag
    db.do_query('delete_post_tags_by_post_id', {
        'post_id': post_id,
    })

    # insert new
    db.do_query('insert_tag', tags)
    return flask.jsonify({'post_id': post_id})
