''' make and parse JWT, compatible with BSON '''

import os
from datetime import datetime, timedelta
import jwt.api_jws as jws
from bson import json_util
from flask import current_app


_SECRET_KEY = os.environ['FLASK_JWT_KEY']


def make_token(data, valid_duration=24*60*60):
    json_data = json_util.dumps(data)
    token = jws.encode(
        json_data.encode(),
        _SECRET_KEY,
        headers={
            'exp': str(datetime.utcnow() + timedelta(seconds=valid_duration))
        })
    return token.decode()


def parse_token(token):
    try:
        byte_token = jws.decode(token, _SECRET_KEY)
        return json_util.loads(byte_token)
    except Exception:
        return None
