''' combine all seeds to reset database to prototype '''

from utils import mongo_client, MONGO_COLLECTION
from .users_seed import users_seed


def reset_database():
    # drop old data
    mongo_client.drop_database(MONGO_COLLECTION)

    # seeds
    users_seed()
