from flask import request
from flask_restful import Resource
import json

class DeviceResource(Resource):
    def __init__(self, device):
        self.device = device


    def post(self):
        action = request.json['action']
        if self.device.trigger_action(action):
            return 200
        return 400
