from flask import Flask, send_file, redirect
from utils import Logger
from database.seeders import reset_database

# init
app = Flask(__name__, static_folder='../template/static')
app.url_map.strict_slashes = False
Logger.init(app)

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

# register blueprints
from routes import blueprints
for bp in blueprints:
    app.register_blueprint(bp)

# start server
if __name__ == '__main__':
    app.run()
