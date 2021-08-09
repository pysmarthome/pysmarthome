from flask import request
from flask_restful import Resource
import json

from .device import DeviceResource


class PCLampResource(DeviceResource):
    def post(self):
        return super().post()
