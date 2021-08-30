from flask import Request, Response
import json


class Auth:
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


def register_middlewares(app):
    app.wsgi_app = Auth(app.wsgi_app, app.config['API_KEY'])
