from pysmarthome import DevicesModel
from durc import Model, clone


class PcActions(Model):
    schema = Model.schema | {
        'name': { 'type': 'string' },
        'path': { 'type': 'string' },
        'data': { 'type': 'string' },
    }


class PcsModel(DevicesModel):
    schema = clone(DevicesModel.schema) | {
        'addr': { 'type': 'string' },
        'ping_cmd': { 'type': 'string' },
        'mac_addr': { 'type': 'string' },
        'actions_handler_addr': { 'type': 'string' },
        'actions_handler_api_key': { 'type': 'string' },
    }
    children_model_classes = clone(DevicesModel.children_model_classes) | {
        'actions': { 'class': PcActions, 'quantity': '*' },
    }
