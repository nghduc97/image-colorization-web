''' make and parse JWT, compatible with BSON '''

import os
import jwt.api_jws as jws
from bson import json_util


_SECRET_KEY = os.environ['FLASK_JWT_KEY']


def make_token(data):
    json_data = json_util.dumps(data)
    return jws.encode(json_data.encode(), _SECRET_KEY).decode()


def parse_token(token):
    try:
        byte_token = jws.decode(token, _SECRET_KEY)
        return json_util.loads(byte_token)
    except Exception:
        return None
