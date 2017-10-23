''' seed "post_tag" table '''

from database.queries import do_query


def post_tag_seed():
    for i in range(25):
        do_query('insert_tag', {
            'post_id': i % 10 + 1,
            'tag': 'tag-{}'.format(i)
        })
