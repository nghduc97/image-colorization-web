''' /api/post routes controller '''

from flask import Blueprint
from utils import mongo


post_blueprint = Blueprint("post", __name__, url_prefix="/api/post")


@post_blueprint.route('/top', methods=["GET"])
def get_top_posts():
    mongo["posts"].find().sort({})
