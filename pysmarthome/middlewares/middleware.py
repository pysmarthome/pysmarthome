from flask import Request, Response
import json
import os


class Middleware:
    def __init__(self, app, api_key):
        self.app = app
        self.api_key = api_key


    def __call__(self, env, start_response):
        request = Request(env)
        if 'Authorization' not in request.headers or \
            request.headers['Authorization'] != self.api_key:
            res = Response(
                json.dumps({
                    'message': 'Not Authorized',
                }),
                mimetype='application/json',
                status=401
            )
            return res(env, start_response)
        return self.app(env, start_response)


def register_middleware(app):
    api_key = os.getenv('PYSMARTHOME_API_KEY')
    app.wsgi_app = Middleware(app.wsgi_app, api_key)
