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
    }
    children_model_classes = {
        'state':  { 'class': DeviceStatesModel, 'quantity': '1' },
    }
