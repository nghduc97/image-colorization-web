''' export all SQL query methods '''
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import os
from sqlalchemy import create_engine, sql
import utils.file as file


url = 'postgresql+pygresql://{0}:{1}@{2}:{3}/{0}'.format(
    os.environ['POSTGRES_USER'],
    os.environ['POSTGRES_PASSWORD'],
    'db',
    os.environ['POSTGRES_PORT'],
)
conn = create_engine(url, echo=(os.environ['FLASK_DEBUG'] == '1')) \
    .connect() \
    .execution_options(autocommit=True)

# cache queries in memory
queries = dict()


def do_query(name, params):
    if name not in queries:
        path = os.path.join(os.path.dirname(__file__), 'templates/{}.sql'.format(name))
        # no cache in DEBUG mode
        if os.environ['FLASK_DEBUG'] == '1':
            return conn.execute(sql.text(file.read_text(path)), params)

        # cahe in PRODUCTION mode
        queries[name] = file.read_text(path)

    return conn.execute(sql.text(queries[name]), params)


def query_fetchone(name, params):
    return dict(do_query(name, params).fetchone())


def query_fetchall(name, params):
    return [dict(row) for row in do_query(name, params).fetchall()]


def do_schema_scripts():
    path = os.path.join(os.path.dirname(__file__), 'schemas/schema.sql')
    query = file.read_text(path)
    # TODO: do all migrations
    return conn.execute(sql.text(query))
