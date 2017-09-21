''' types of response '''

from flask import Response
from .token_parser import make_token
from server.utils import ejson


def token_response(obj):
    ''' send response as JWT '''
    return Response(make_token(obj), mimetype='text/plain')


def ejson_response(obj):
    ''' Extended json type response '''
    return Response(
        ejson.stringify(obj),
        mimetype='application/json-extended'
    )
