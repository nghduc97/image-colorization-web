''' /api/post routes controller '''

from flask import Blueprint
from server.utils.mongo import mongo
from server.utils.response import ejson_response


post_blueprint = Blueprint("post", __name__, url_prefix="/api/post")


@post_blueprint.route('/top', methods=["GET"])
def get_top_posts():
    cursor = mongo["posts"].find({
        'hidden': False
    }).sort('time', -1).limit(5)

    return ejson_response(list(cursor))
