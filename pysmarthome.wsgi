#!/usr/bin/env python
from pysmarthome import app as application, config

if __name__ == '__main__':
    application.run(host=config['host'], port=config['port'])
