''' seed "posts" table '''

from datetime import datetime, timedelta
import database.queries as db


def posts_seed():
    for i in range(8):
        db.do_query('insert_image_post', {
            'hidden': False,
            'time': (datetime.utcnow() - timedelta(hours=i)),
            'uploader_id': i + 1,
            'title': 'Post #{}'.format(i),
            'total_claps': 0,
            'status': 'complete',
        })

    for i in range(8, 10):
        db.do_query('insert_discuss_post', {
            'hidden': False,
            'time': (datetime.utcnow() - timedelta(hours=i)),
            'uploader_id': i + 1,
            'title': 'Post #{}'.format(i),
            'total_claps': 0,
            'content': 'discuss post #{}'.format(i),
        })
