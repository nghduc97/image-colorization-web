from flask import Flask, send_file
import sys

app = Flask(__name__, static_folder='../template/static')
app.url_map.strict_slashes = False

@app.route('/', methods=["GET"])
def index():
    return send_file("../template/index.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
