''' utils for JSON extended '''

from bson import json_util
from flask import request


def parse(text):
    return json_util.loads(text, json_options=json_util.CANONICAL_JSON_OPTIONS)


def stringify(obj):
    return json_util.dumps(obj, json_options=json_util.CANONICAL_JSON_OPTIONS)


def ejson_route(func):
    def wrapper(*args, **kwargs):
        request.data = parse(request.data)
        return func(*args, **kwargs)
    return wrapper
