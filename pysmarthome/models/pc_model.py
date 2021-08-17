from .device_model import DeviceModel
from .model import Model


class PcActions(Model):
    schema = Model.schema | {
        'actions': {
            'type': 'dict',
            'allow_unknown': {
                'type': 'dict',
                'schema': {
                    'name': { 'type': 'string' },
                    'path': { 'type': 'string' },
                    'data': { 'type': 'string' },
                },
            },
        },
    }
    collection = 'pc_actions'


    def get(self, id):
        if id in self.actions:
            return self.actions[id]
        return None


class PcModel(DeviceModel):
    schema = DeviceModel.schema | {
        'actions_handler': {
            'type': 'dict',
            'schema': {
                'addr': { 'type': 'string' },
                'api_key': { 'type': 'string' },
            },
        },
    }
    children_model_classes = DeviceModel.children_model_classes | {
        'actions': PcActions
    }
