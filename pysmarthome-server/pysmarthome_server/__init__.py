from flask import Flask, g
from .middlewares import register_middlewares
from .endpoints import register_endpoints
from pysmarthome_lib import PluginController
from .factories import DevicesFactory
from .db import db
from .config import config

app = Flask(__name__)
app.config['API_KEY'] = config['api_key']
register_middlewares(app)
conn = db.init(config['db'])
plugins = PluginController.load_all(conn)
DevicesFactory.init(plugins)
register_endpoints(app)


@app.before_request
def before_request():
    g.db = conn

@app.teardown_request
def teardown_request(exception):
    g.pop('db', None)

