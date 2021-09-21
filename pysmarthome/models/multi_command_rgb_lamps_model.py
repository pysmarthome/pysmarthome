from .rgb_light_model import RgbLampsModel
from .multi_command_devices_model import MultiCommandDevicesModel, CommandsModel
from .colors_model import ColorsModel
from durc import Model, clone


class ColorCommandsModel(Model):
    children_model_classes = {
        'color': { 'class': ColorsModel, 'quantity': 1 },
        'command': { 'class': CommandsModel, 'quantity': 1 },
    }

    def to_dict(self):
        return {
            **super().to_dict(),
            'color': self.color.to_dict(),
            'command': self.command.to_dict(),
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
