''' seed "comments" collection '''

from datetime import datetime, timedelta
from bson import ObjectId
from server.utils.mongo import mongo


def comments_seed():
    # get collection
    collection = mongo['comments']

    # indexes
    collection.create_index({'user_id': 1, 'time': -1})
    collection.create_index({'post_id': 1, 'time': -1})

    # data
    comments = []
    for i in range(100):
        comments.append()

    collection.insert_many(comments)
