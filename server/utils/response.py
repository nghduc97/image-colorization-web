''' types of response '''

from flask import Response
from bson import json_util
from .token_parser import make_token


def token_response(obj):
    ''' send response as JWT '''
    return Response(make_token(obj), mimetype='text/plain')


def ejson_response(obj):
    ''' Extended json type response '''
    return Response(
        json_util.dumps(obj, json_options=json_util.CANONICAL_JSON_OPTIONS),
        mimetype='application/json-extended'
    )
