from flask import Flask, send_file
import sys

# init
app = Flask(__name__, static_folder='../template/static')
app.url_map.strict_slashes = False

# index route
@app.route('/', methods=["GET"])
def index():
    return send_file("../template/index.html")

if __name__ == '__main__':
    app.run()
