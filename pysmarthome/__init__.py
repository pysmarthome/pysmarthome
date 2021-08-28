from flask import Flask, g
from .factories import ManagersFactory
from .middlewares import register_middlewares
from .endpoints import register_endpoints
from .db import db
from .config import config


app = Flask(__name__)
app.config['API_KEY'] = config['api_key']
db = db.init(config['db'])
ManagersFactory.init_all(db)

register_middlewares(app)
register_endpoints(app)


@app.before_request
def before_request():
    g.db = db

@app.teardown_request
def teardown_request(exception):
    g.pop('db', None)
