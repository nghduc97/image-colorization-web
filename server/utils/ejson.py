''' utils for JSON extended '''

from bson import json_util


def parse(text):
    return json_util.loads(text, json_options=json_util.CANONICAL_JSON_OPTIONS)


def stringify(obj):
    return json_util.dumps(obj, json_options=json_util.CANONICAL_JSON_OPTIONS)
