from .managers import BroadlinkManager
from .controllers import AcController, TvController, BroadlinkDeviceController
from .controllers import BroadlinkRgbLampController

config = {
    'addr': { 'type': 'string', 'required': True }
}

device_controllers = [
    AcController,
    TvController,
    BroadlinkDeviceController,
    BroadlinkRgbLampController,
]


def on_load(**data):
    BroadlinkManager.init_client(**data)
