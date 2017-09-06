from flask import Flask, render_template
import sys

app = Flask(__name__, template_folder='../client/dist', static_folder='../client/dist/static')
app.url_map.strict_slashes = False

try:
    sys.argv.index("production")
    app.debug = False
except:
    app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8050)
