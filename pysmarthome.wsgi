#!/usr/bin/env python
import os
import sys
from pysmarthome import run_server

config_path = os.path.join(os.getenv('HOME'), '.config', 'pysmarthome')
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

if __name__ == '__main__':
    run_server(**config)
