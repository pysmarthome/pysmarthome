import base64
from .model import Model
from .device_model import DeviceModel
from .rgb_light_model import RgbLightModel, RgbLightStateModel

class BroadlinkCommands(Model):
    schema = {
        **Model.schema,
        'commands': {
            'type': 'dict',
            'valuesrules': {
                'type': 'string',
            },
        }
    }
    collection = 'broadlink_commands'


    def get(self, id):
        if id in self.commands:
            return base64.b64decode(self.commands[id])
        return None


    def set(self, id, data):
        self.commands[id] = data


class BroadlinkDeviceModel(DeviceModel):
    schema = DeviceModel.schema
    children_model_classes = DeviceModel.children_model_classes | {
        'commands': BroadlinkCommands
    }


class BroadlinkRgbLightModel(BroadlinkDeviceModel, RgbLightModel):
    schema = {
        **RgbLightModel.schema,
        **BroadlinkDeviceModel.schema
    }
    state_model = RgbLightStateModel
