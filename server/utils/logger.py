# to avoid importing from main.py
from io import StringIO
from pprint import pprint

class Logger:
    def init(app):
        Logger.logger = app.logger
    
    def to_pretty_string(item):
        stream = StringIO()
        pprint(item, stream=stream)
        value = stream.getvalue()
        stream.close()
        return value

    def info(item):
        Logger.logger.info(Logger.to_pretty_string(item))
