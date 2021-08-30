#!/usr/bin/env python
from pysmarthome_server import app as application, config

if __name__ == '__main__':
    application.run(host=config['host'], port=config['port'])
