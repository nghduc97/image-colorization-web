from flask import Flask, send_file, redirect
from utils import Logger

# init
app = Flask(__name__, static_folder='../template/static')
app.url_map.strict_slashes = False
Logger.init(app)

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
