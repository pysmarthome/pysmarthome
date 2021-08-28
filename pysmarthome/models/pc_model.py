from pysmarthome.config import collections
from .device_model import DeviceModel
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
    collection = collections['pc_actions']


    def get(self, id):
        if id in self.actions:
            return self.actions[id]
        return None


class PcModel(DeviceModel):
    schema = clone(DeviceModel.schema) | {
        'actions_handler': {
            'type': 'dict',
            'schema': {
                'addr': { 'type': 'string' },
                'api_key': { 'type': 'string' },
            },
        },
    }
    collection = collections['pcs']
    children_model_classes = clone(DeviceModel.children_model_classes)
    children_model_classes |= { 'actions': { 'class': PcActions } }
    children_model_classes['collection_ref']['attrs'] = collection
