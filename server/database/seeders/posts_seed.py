''' seed "posts" collection '''

from base64 import b64encode
from datetime import datetime, timedelta
from server.utils.mongo import mongo


def posts_seed():
    # get collection
    collection = mongo['posts']

    # indexes
    collection.create_index([
        ('hidden', 1),
        ('time', -1),
    ])

    collection.create_index([
        ('hidden', 1),
        ('claps', -1),
    ])

    collection.create_index([
        ('hidden', 1),
        ('uploader_id', 1),
        ('time', -1),
    ])

    collection.create_index([
        ('hidden', 1),
        ('uploader_id', 1),
        ('claps', -1),
    ])

    collection.create_index([
        ('hidden', 1),
        ('title', 'text'),
        ('tags', 'text'),
    ])

    # base64 image
    img0 = None
    with open('./database/seeders/seed_assets/0.jpg', 'rb') as file:
        img0 = b64encode(file.read()).decode('utf8')

    img1 = None
    with open('./database/seeders/seed_assets/1.jpg', 'rb') as file:
        img1 = b64encode(file.read()).decode('utf8')

    # data
    posts = []
    for i in range(10):
        posts.append({
            'hidden': i < 2,
            'time': datetime.utcnow() - timedelta(hours=i),
            'uploader_id': mongo['users'].find_one({'username': 'dummy' + str(i)})['_id'],
            'title': 'post' + str(i),
            'claps': 0,
            'tags': [],
            'original_image': img0 if i < 5 else img1
        })

    collection.insert_many(posts)
