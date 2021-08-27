from flask import Flask, g

from .middlewares import register_middlewares
from .endpoints import register_endpoints
from .db import s3db
from .config import config


app = Flask(__name__)
app.config['API_KEY'] = config['api_key']
db = s3db(config['s3db'])
register_middlewares(app)


@app.before_request
def before_request():
    g.db = db

@app.teardown_request
def teardown_request(exception):
    g.pop('db', None)


def run_server(host='0.0.0.0', port=5000, **config):
    app.run(host=host, port=port)
