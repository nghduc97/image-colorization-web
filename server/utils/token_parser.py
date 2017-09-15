from . import mongo
from bson import json_util
from jwt.api_jws import encode, decode
import os
from utils import Logger

_secret_key = os.environ['FLASK_JWT_KEY']

def make_token(data):
    json_data = json_util.dumps(data)
    return encode(json_data.encode(), _secret_key)

def parse_token(token):
    try:
        json_data = decode(token, _secret_key)
        return json_util.loads(json_data.decode())
    except Exception:
        return None
