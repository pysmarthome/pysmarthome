from .model import Model

class DeviceStateModel(Model):
    schema = {
        **Model.schema,
        'state': {
            'type': 'dict',
            'schema': {
                'power': {
                    'type':  'string',
                    'allowed': ['on', 'off'],
                    'required': True
                },
            }
        }
    }
    collection = 'devices_states'


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
    collection = 'devices'
    children_model_classes = { 'state':  DeviceStateModel }
