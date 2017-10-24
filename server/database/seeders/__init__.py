''' export method to reset database to prototype '''
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import time
from database.queries import do_schema_scripts
import utils.file as file
from .users_seed import users_seed
from .posts_seed import posts_seed
from .comments_seed import comments_seed
from .claps_seed import claps_seed
from .post_tag_seed import post_tag_seed


def reset_database():
    # recreate schema
    do_schema_scripts()

    # seeds
    users_seed()
    posts_seed()
    comments_seed()
    claps_seed()
    post_tag_seed()
