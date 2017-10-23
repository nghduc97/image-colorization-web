''' seed "claps" table '''

from database.queries import do_query


def claps_seed():
    for i in range(100):
        do_query('upsert_clap', {
            'user_id': i % 10 + 1,
            'post_id': i // 10 + 1,
            'amount': i % 60,
        })
