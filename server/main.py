import os
from flask import Flask, send_file, redirect
from database.seeders import reset_database
from routes import blueprints

# init
app = Flask(__name__, static_folder='../template/static')
app.url_map.strict_slashes = False


# CLI
@app.cli.command()
def resetdb():
    reset_database()


# index route
@app.route('/', methods=["GET"])
def index():
    return send_file("../template/index.html")


# to index route on irregular URL
@app.errorhandler(404)
def to_index(err):
    return redirect('/')


# modify headers before sending responses
@app.after_request
def map_response(res):
    if os.environ['FLASK_DEBUG'] == '1':
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        res.headers['Access-Control-Allow-Origin'] = '*'
    return res


# register blueprints
for bp in blueprints:
    app.register_blueprint(bp)


# start server
if __name__ == '__main__':
    app.run()
