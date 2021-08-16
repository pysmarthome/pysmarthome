from .device_model import DeviceModel, DeviceStateModel


class RgbLightStateModel(DeviceStateModel):
    schema = DeviceStateModel.schema
    schema['state']['schema'] |= {
        'color': { 'type': 'string' },
        'brightness': { 'type': 'number' },
    }


class RgbLightModel(DeviceModel):
    state_model = RgbLightStateModel
