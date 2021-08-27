from pysmarthome.config import collections
from .model import Model, clone
from .refs import DevicesRefModel


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
        'addr': { 'type': 'string' },
        'mac_addr': { 'type': 'string' },
        'api_key': { 'type': 'string' },
    }
    children_model_classes = {
        'state':  { 'class': DeviceStateModel },
        'collection_ref': { 'class': DevicesRefModel },
    }


class SonoffModel(DeviceModel):
    collection = collections['sonoffs']
    children_model_classes = clone(DeviceModel.children_model_classes)
    children_model_classes['collection_ref']['attrs'] = collection
