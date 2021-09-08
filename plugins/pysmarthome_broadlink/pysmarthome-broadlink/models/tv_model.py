from pysmarthome import DeviceStatesModel, clone
from .broadlink_model import BroadlinkDevicesModel

class TvStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100, 'default': 0 },
        'mute': { 'type': 'boolean', 'default': False },
    }
    collection = DeviceStatesModel.collection


class TvsModel(BroadlinkDevicesModel):
    schema = clone(BroadlinkDevicesModel.schema) |  {
        'addr': { 'type': 'string' },
        'ping_cmd': { 'type': 'string' },
    }
    children_model_classes = clone(BroadlinkDevicesModel.children_model_classes)
    children_model_classes['state']['class'] = TvStatesModel
