''' seed "comments" table '''

from datetime import datetime
from database.queries import do_query


def comments_seed():
    for i in range(100):
        do_query('insert_comment', {
            'user_id': i % 10 + 1,
            'post_id': i // 10 + 1,
            'content': 'Comment #{}'.format(i),
            'time': datetime.utcnow(),
        })
