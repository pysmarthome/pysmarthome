import base64
from vesla_pymvc import Model, clone
from pysmarthome_lib import DevicesModel

class BroadlinkCommandsModel(Model):
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


class BroadlinkRgbLampCommands(BroadlinkCommandsModel):
    schema = clone(BroadlinkCommandsModel.schema)
    schema['commands']['valuesrules']['schema'] |= {
        'hex': { 'type': 'string' },
    }
    collection = BroadlinkCommandsModel.collection


    def hex(self, id):
        if id in self.commands:
            return self.commands[id]['hex']
        return None


    def colors(self):
        return dict([(k, {
            'name': v['name'],
            'hex': v['hex'],
        }) for k, v in self.commands.items() if 'hex' in v])



class BroadlinkDevicesModel(DevicesModel):
    schema = clone(DevicesModel.schema)
    children_model_classes = clone(DevicesModel.children_model_classes) | {
        'commands': { 'class': BroadlinkCommandsModel },
    }
