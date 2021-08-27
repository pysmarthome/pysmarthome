from .device_model import DeviceModel, DeviceStateModel, clone

class RgbLightStateModel(DeviceStateModel):
    schema = clone(DeviceStateModel.schema)
    schema['state']['schema'] |= {
        'color': { 'type': 'string', 'default': '#ffffff' },
        'brightness': { 'type': 'number', 'default': 0 },
    }


class RgbLightModel(DeviceModel):
    schema = clone(DeviceModel.schema)
    children_model_classes = clone(DeviceModel.children_model_classes)
    children_model_classes |= { 'state': { 'class': RgbLightStateModel } }


