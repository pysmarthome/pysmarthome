import base64
from vesla_pymvc import Model, clone
from .device_model import DeviceModel
from .rgb_light_model import RgbLightModel, RgbLightStateModel
from pysmarthome.config import collections

class BroadlinkCommands(Model):
    schema = {
        **Model.schema,
        'commands': {
            'type': 'dict',
            'default': {},
            'valuesrules': {
                'type': 'dict',
                'schema': {
                    'name': { 'type': 'string' },
                    'data': { 'type': 'string' },
                },
            },
        }
    }
    collection = collections['broadlink_commands']


    def get(self, id):
        if id in self.commands:
            return base64.b64decode(self.commands[id]['data'])
        return None


    def name(self, id):
        if id in self.commands:
            return self.commands[id]['name']
        return None


    def set(self, id, data):
        self.commands[id] = data


class BroadlinkRgbLightCommands(BroadlinkCommands):
    schema = clone(BroadlinkCommands.schema)
    schema['commands']['valuesrules']['schema'] |= {
        'hex': { 'type': 'string' },
    }


    def hex(self, id):
        if id in self.commands:
            return self.commands[id]['hex']
        return None


    def colors(self):
        return dict([(k, {
            'name': v['name'],
            'hex': v['hex'],
        }) for k, v in self.commands.items() if 'hex' in v])


class BroadlinkDeviceModel(DeviceModel):
    schema = clone(DeviceModel.schema)
    children_model_classes = clone(DeviceModel.children_model_classes) | {
        'commands': { 'class': BroadlinkCommands },
    }


class BroadlinkRgbLightModel(BroadlinkDeviceModel, RgbLightModel):
    schema = clone(RgbLightModel.schema) | clone(BroadlinkDeviceModel.schema)
    collection = collections['broadlink_lamps']
    children_model_classes = clone(BroadlinkDeviceModel.children_model_classes)
    children_model_classes |= {
        'commands': { 'class': BroadlinkRgbLightCommands },
        'state': { 'class': RgbLightStateModel },
    }
    children_model_classes['collection_ref']['attrs'] = collection
