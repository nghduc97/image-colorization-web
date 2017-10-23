''' /api/post routes controller '''

import flask


post_blueprint = flask.Blueprint("post", __name__, url_prefix="/api/post")


@post_blueprint.route('/top', methods=["GET"])
def get_top_posts():
    pass
