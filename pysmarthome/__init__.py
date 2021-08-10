import os
import sys
from flask import Flask

from .managers import DevicesManager
from .middlewares.middleware import register_middleware
from .init_devices import init_devices
from .endpoints import register_endpoints

config_path = os.path.join(os.getenv('HOME'), '.config', __name__)
if not os.path.exists(config_path):
    os.makedirs(config_path)

config_file_path = os.path.join(config_path, 'config.py')
if not os.path.exists(config_file_path):
    pkg_dir = os.path.dirname(__file__)
    with open(os.path.join(pkg_dir, 'config.example.py')) as f:
        cfg_example = f.read()
    with open(config_file_path, 'w') as f:
        f.write(cfg_example)

sys.path.append(config_path)
from config import config

app = Flask(__name__)
register_middleware(app)
devices_manager = DevicesManager()
init_devices(devices_manager, config)
api = register_endpoints(app, devices_manager)


def run_server():
    app.run('0.0.0.0', port=config['port'])
