from durc import Model
from .device_model import DevicesModel


class ScenesModel(Model):
    schema = {
        **Model.schema,
        'name': { 'type': 'string', 'required': True },
        'snapshot_state_ids': {
            'type': 'list',
            'schema': { 'type': 'string' },
            'required': True,
        },
        'device_ids': {
            'type': 'list',
            'schema': { 'type': 'string' },
            'required': True,
        },
    }
