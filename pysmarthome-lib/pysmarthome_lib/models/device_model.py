from vesla_pymvc import Model
from .refs_model import RefModel


class DeviceStatesModel(Model):
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


class DevicesModel(Model):
    schema = {
        **Model.schema,
        'name': {
            'type': 'string',
            'required': True,
        },
        'addr': { 'type': 'string' },
        'ping_cmd': { 'type': 'string' },
        'mac_addr': { 'type': 'string' },
        'api_key': { 'type': 'string' },
    }
    children_model_classes = {
        'state':  { 'class': DeviceStatesModel },
        'collection_ref': { 'class': RefModel.clone('DevicesRefModel') },
    }
