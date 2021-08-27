from flask import request, g
from flask_restful import Resource
import json
from pysmarthome.factories.devices_factory import DevicesFactory


class StatesResource(Resource):
    def get(self, id=''):
        if id:
            return DevicesFactory.load(g.db, id).state.to_dict()
        return [ d.state.to_dict() for d in DevicesFactory.load_all(g.db) ]


    def post(self, id):
        dev = DevicesFactory.load(g.db, id)
        data = request.json['data']
        dev.set_state(**data)
        return dev.state.to_dict()
