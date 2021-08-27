from flask import Flask

from .managers import DevicesManager
from .middlewares import register_middlewares
from .endpoints import register_endpoints
from .db import s3db
from .config import config


app = Flask(__name__)
app.config['API_KEY'] = config['api_key']
register_middlewares(app)

def run_server(host='0.0.0.0', port=5000, **config):
    db = s3db(**config['db'])
    devices_manager = DevicesManager(db)

    app.run(host=host, port=port)
