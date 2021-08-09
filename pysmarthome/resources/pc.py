from flask import request
from flask_restful import Resource
import json

from .device import DeviceResource

class PCResource(DeviceResource):
    def post(self, device='', id=''):
        action = request.json['action']
        if self.device.trigger_action(action, device, id):
            return 200
        return 400
