''' seed "users" table '''

import werkzeug.security as security
import database.queries as db


def users_seed():
    for i in range(10):
        db.do_query('insert_user', {
            'display_name': 'Dummy #{}'.format(i),
            'authority': 4,
            'username': 'dummy{}'.format(i),
            'hashed_password': security.generate_password_hash('dummy{}'.format(i), salt_length=32),
        })
