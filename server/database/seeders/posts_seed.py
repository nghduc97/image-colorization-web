''' seed "posts" table '''

import os
import shutil
from datetime import datetime, timedelta
import database.queries as db


def posts_seed():
    dir_name = os.path.join(os.path.dirname(__file__), 'seed_assets')
    img_original = os.path.join(dir_name, '0.jpeg')
    img_painted = os.path.join(dir_name, '1.jpeg')

    for i in range(8):
        db.do_query('insert_image_post', {
            'hidden': i < 2,
            'time': (datetime.utcnow() - timedelta(hours=i)),
            'uploader_id': i + 1,
            'title': 'Post #{}'.format(i),
            'total_claps': 0,
            'status': 'done',
        })
        shutil.copyfile(img_original, '/storage/image_posts/original/{}.jpeg'.format(i + 1))
        shutil.copyfile(img_painted, '/storage/image_posts/painted/{}.jpeg'.format(i + 1))

    for i in range(8, 10):
        db.do_query('insert_discuss_post', {
            'hidden': False,
            'time': (datetime.utcnow() - timedelta(hours=i)),
            'uploader_id': i + 1,
            'title': 'Post #{}'.format(i),
            'total_claps': 0,
            'content': 'discuss post #{}'.format(i),
        })
