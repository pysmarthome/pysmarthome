from .device_model import DevicesModel, DeviceStatesModel
from durc import clone


class AcStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'temp': { 'type': 'integer', 'default': 16 },
    }
    collection = DeviceStatesModel.collection


class AcsModel(DevicesModel):
    schema = clone(DevicesModel.schema) | {
        'temp_max': { 'type': 'integer', 'default': 24 },
        'temp_min': { 'type': 'integer', 'default': 16 },
    }
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes['state']['class'] = AcStatesModel
