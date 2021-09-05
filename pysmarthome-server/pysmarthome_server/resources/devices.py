from flask import request, g
from flask_restful import Resource
import json

class DevicesResource(Resource):
    def get(self, id=''):
        if id:
            return g.dev_controllers[id].to_dict()
        return [ d.to_dict() for d in g.dev_controllers.values() ]


    def post(self, id):
        dev = g.dev_controllers[id]
        res = {
            'status': 400,
            'body': ''
        }
        if 'data' in request.json:
            data = request.json['data']
            dev.update(**data)
            res['body'] = dev.to_dict()
            res['status'] = 200
        if dev and 'action' in request.json:
            action = request.json['action']
            args = []
            if 'args' in request.json:
                args = request.json['args']
            if dev.trigger_action(action, *args):
                res['body'] = dev.state.to_dict()
                res['status'] = 200
        return res
