from flask import Flask, g
from .middlewares import register_middlewares
from .endpoints import register_endpoints
from pysmarthome_lib import PluginManager
from .db import db
from .config import config

app = Flask(__name__)
app.config['API_KEY'] = config['api_key']
register_middlewares(app)
conn = db.init(config['db'])
dev_controllers = PluginManager.init(conn)
register_endpoints(app)


@app.before_request
def before_request():
    g.dev_controllers = dev_controllers

@app.teardown_request
def teardown_request(exception):
    g.pop('dev_controllers', None)

