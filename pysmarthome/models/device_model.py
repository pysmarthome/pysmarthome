from pysmarthome.config import collections
from .model import Model, clone

class DeviceStateModel(Model):
    schema = {
        **Model.schema,
        'state': {
            'type': 'dict',
            'default': {},
            'required': True,
            'schema': {
                'power': {
                    'type':  'string',
                    'allowed': ['on', 'off'],
                    'default': 'off',
                    'required': True
                },
            }
        }
    }
    collection = collections['states']


class DeviceModel(Model):
    schema = {
        **Model.schema,
        'name': {
            'type': 'string',
            'required': True,
        },
        'controller': {
            'type': 'string',
            'allowed': [
                'tv',
                'ac',
                'broadlink_rgb_lamp',
                'broadlink',
                'yeelight',
                'sonoff',
                'pc',
                'govee',
            ],
            'required': True,
        },
        'addr': { 'type': 'string' },
        'mac_addr': { 'type': 'string' },
        'api_key': { 'type': 'string' },
    }
    children_model_classes = { 'state':  DeviceStateModel }


class SonoffModel(DeviceModel):
    collection = collections['sonoffs']
    children_model_classes = clone(DeviceModel.children_model_classes)
