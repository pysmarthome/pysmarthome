from pysmarthome_lib import DevicesModel
from vesla_pymvc import Model, clone


class PcActions(Model):
    schema = Model.schema | {
        'actions': {
            'type': 'dict',
            'allow_unknown': {
                'type': 'dict',
                'default': {},
                'schema': {
                    'name': { 'type': 'string' },
                    'path': { 'type': 'string' },
                    'data': { 'type': 'string' },
                },
            },
        },
    }


    def get(self, id):
        if id in self.actions:
            return self.actions[id]
        return None


class PcsModel(DevicesModel):
    schema = clone(DevicesModel.schema) | {
        'actions_handler': {
            'type': 'dict',
            'schema': {
                'addr': { 'type': 'string' },
                'api_key': { 'type': 'string' },
            },
        },
    }
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes |= { 'actions': { 'class': PcActions } }
