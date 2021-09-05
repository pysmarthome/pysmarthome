from flask import request, g
from flask_restful import Resource
import json


class StatesResource(Resource):
    def get(self, id=''):
        if id:
            return g.dev_controllers[id].state.to_dict()
        return [ d.state.to_dict() for d in g.dev_controllers.values() ]


    def post(self, id):
        dev = g.dev_controllers[id]
        data = request.json['data']
        dev.set_state(**data)
        return dev.state.to_dict()
