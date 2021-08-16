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
