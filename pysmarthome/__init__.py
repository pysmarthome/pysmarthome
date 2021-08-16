from flask import Flask

from .managers import DevicesManager
from .middlewares import register_middleware
from .endpoints import register_endpoints
from .db import s3db

def run_server(host='0.0.0.0', port=5000, **config):
    app = Flask(__name__)
    register_middleware(app)
    db = s3db(**config['db'])
    devices_manager = DevicesManager(db)

    app.run(host=host, port=port)
