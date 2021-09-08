from .device_model import DevicesModel, DeviceStatesModel
from durc import clone


class RgbLampStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'color': { 'type': 'string', 'default': '#ffffff' },
        'brightness': { 'type': 'number', 'default': 0 },
    }
    collection = DeviceStatesModel.collection


class RgbLampsModel(DevicesModel):
    schema = clone(DevicesModel.schema)
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes['state']['class'] = RgbLampStatesModel
