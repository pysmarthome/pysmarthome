from durc import clone, Model
from hashlib import md5
import json

class DeviceStatesModel(Model):
    schema = {
        **Model.schema,
        'power': {
            'type':  'string',
            'allowed': ['on', 'off'],
            'default': 'off',
            'required': True
        },
    }


class SnapshotStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema)
    id_setter = lambda x: md5(json.dumps(dict(sorted(x.items()))).encode()).hexdigest()
    schema['id']['default_setter'] = id_setter
    del schema['power']['required']
    del schema['power']['default']

    @property
    def actions(self):
        actions = []
        attrs = self.attrs
        if 'power' in attrs:
            actions.append((self.power,))
        return actions


class DevicesModel(Model):
    schema = {
        **Model.schema,
        'name': {
            'type': 'string',
            'required': True,
        },
        'addr': { 'type': 'string', 'default': '' },
        'power_by_ping': { 'type': 'boolean', 'default': False },
    }
    children_model_classes = {
        'state':  { 'class': DeviceStatesModel, 'quantity': '1' },
    }
