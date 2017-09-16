from pymongo import ASCENDING
from utils import mongo
from werkzeug.security import generate_password_hash

def users_seed():
    # indexes
    mongo['users'].create_index('username', unique=True)

    # data
    users = []
    for i in range(10):
        users.append({
            'username': 'dummy{}'.format(i),
            'hashed_password': generate_password_hash('dummy{}'.format(i)),
            'display_name': 'Dummy #{}'.format(i),
            'authority': 4
        })

    mongo['users'].insert_many(users)
