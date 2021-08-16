from .device_model import DeviceStateModel
from .broadlink_model import BroadlinkDeviceModel

class AcStateModel(DeviceStateModel):
    schema = DeviceStateModel.schema
    schema['state']['schema'] |= {
        'temp': { 'type': 'integer', 'min': 16, 'max': 24 },
    }


class AcModel(BroadlinkDeviceModel):
    state_model = AcStateModel
