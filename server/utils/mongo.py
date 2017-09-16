from pymongo import MongoClient
import os

MONGO_HOST_NAME = os.environ["MONGO_HOST_NAME"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_COLLECTION = os.environ["MONGO_COLLECTION"]
mongo_client = MongoClient("mongodb://{0}:{1}/".format(MONGO_HOST_NAME, MONGO_PORT))
mongo = mongo_client[MONGO_COLLECTION]
