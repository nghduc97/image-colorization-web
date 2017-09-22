''' export list of blueprints '''

from .user import user_blueprint
from .post import post_blueprint


blueprints = [
    user_blueprint,
    post_blueprint,
]
