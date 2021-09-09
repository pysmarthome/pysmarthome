from .device_model import DevicesModel, DeviceStatesModel
from durc import clone


class TvStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100, 'default': 0 },
        'mute': { 'type': 'boolean', 'default': False },
    }
    collection = DeviceStatesModel.collection


class TvsModel(DevicesModel):
    schema = clone(DevicesModel.schema) | {
        'volume_max': { 'type': 'integer', 'default': 100 },
        'volume_min': { 'type': 'integer', 'default': 0 },
    }
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes['state']['class'] = TvStatesModel
