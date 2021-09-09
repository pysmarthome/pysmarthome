from durc import Model, clone
from .device_model import DevicesModel


class CommandsModel(Model):
    schema = {
        **Model.schema,
        'name': { 'type': 'string' },
        'label': { 'type': 'string', 'default': '' },
        'data': { 'type': 'string', 'default': '', 'required': True },
    }


class MultiCommandDevicesModel(DevicesModel):
    children_model_classes = clone(DevicesModel.children_model_classes) | {
        'commands': { 'class': CommandsModel, 'quantity': '*' }
    }
