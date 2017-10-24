''' seed "claps" table '''

import database.queries as db


def claps_seed():
    for i in range(100):
        db.do_query('upsert_clap', {
            'user_id': i % 10 + 1,
            'post_id': i // 10 + 1,
            'amount': i % 60,
        })
