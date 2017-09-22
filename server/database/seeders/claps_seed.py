''' seed "claps" collection '''

from datetime import datetime, timedelta
from bson import ObjectId
from server.utils.mongo import mongo


def comments_seed():
    # get collection
    collection = mongo['claps']

    # indexes
    collection.create_index({'user_id': 1, 'post_id': 1})

    # data
    claps = []
    for i in range(100):
        claps.append()

    collection.insert_many(claps)
