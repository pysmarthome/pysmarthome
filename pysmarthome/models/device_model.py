from durc import Model


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
