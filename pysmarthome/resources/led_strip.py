from flask import request
from flask_restful import Resource
import json

class LedStripResource(Resource):
    def __init__(self, devices):
        self.devices = devices


    def post(self, id):
        action = request.json['action']
        if self.devices[f'led_{id}'].trigger_action(action):
            return 200
        return 400
