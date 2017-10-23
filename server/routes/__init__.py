''' export list of blueprints '''
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from .user import user_blueprint
from .post import post_blueprint


blueprints = [
    user_blueprint,
    post_blueprint,
]
