''' methods to validate JSON data from requests '''

from sys import maxsize
from flask import abort


def check_has_fields(json_data, fields):
    for field in fields:
        if (field not in json_data) or (json_data[field] is None):
            abort(400, 'missing field: "{}"'.format(field))


def check_field_length(json_data, field, min_length=None, max_length=None):
    min_length = min_length or 0
    max_length = max_length or maxsize
    data = json_data[field]

    if not isinstance(data, str):
        abort(400, 'field "{}" is not a string'.format(field))

    if min_length > len(data) or len(data) > max_length:
        abort(400, 'field "{0}" should be {1}-{2} characters long'.format(field, min_length, max_length))
