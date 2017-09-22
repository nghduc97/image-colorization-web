''' combine all seeds to reset database to prototype '''

from server.utils.mongo import mongo_client, MONGO_COLLECTION
from .users_seed import users_seed
from .posts_seed import posts_seed


def reset_database():
    # drop old data
    mongo_client.drop_database(MONGO_COLLECTION)

    # seeds
    users_seed()
    posts_seed()
