''' seed "post_tag" table '''

import database.queries as db


def post_tag_seed():
    for i in range(25):
        db.do_query('insert_tag', {
            'post_id': i % 10 + 1,
            'tag': 'tag-{}'.format(i)
        })
