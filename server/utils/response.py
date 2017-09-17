''' types of response '''

from flask import Response
from .token_parser import make_token


def token_response(obj):
    return Response(make_token(obj), mimetype='text/plain')
