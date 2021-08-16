from .device_model import DeviceStateModel
from .broadlink_model import BroadlinkDeviceModel

class TvStateModel(DeviceStateModel):
    schema = DeviceStateModel.schema
    schema['state']['schema'] |= {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100 },
        'mute': { 'type': 'boolean' },
    }


class TvModel(BroadlinkDeviceModel):
    state_model = TvStateModel
