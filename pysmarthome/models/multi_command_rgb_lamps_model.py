from .rgb_light_model import RgbLampsModel
from .multi_command_devices_model import MultiCommandDevicesModel
from durc import Model, clone


class ColorCommandsModel(Model):
    schema = clone(Model.schema) | {
        'color_id': { 'type': 'string', 'required': True },
        'command_id': { 'type': 'string', 'required': True },
    }


class MultiCommandRgbLampsModel(MultiCommandDevicesModel, RgbLampsModel):
    schema = clone(RgbLampsModel.schema) | {
        'brightness_max': { 'type': 'integer', 'default': 100 },
        'brightness_min': { 'type': 'integer', 'default': 0 },
    }
    children_model_classes = clone(MultiCommandDevicesModel.children_model_classes)
    children_model_classes |= clone(RgbLampsModel.children_model_classes) | {
        'color_commands': { 'class': ColorCommandsModel, 'quantity': '*' },
    }
