from pysmarthome.config import collections
from .device_model import DeviceStateModel, DeviceModel, clone
from .broadlink_model import BroadlinkDeviceModel

class TvStateModel(DeviceStateModel):
    schema = clone(DeviceStateModel.schema)
    schema['state']['schema'] |= {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100, 'default': 0 },
        'mute': { 'type': 'boolean', 'default': False },
    }


class TvModel(BroadlinkDeviceModel):
    schema = clone(BroadlinkDeviceModel.schema)
    collection = collections['tvs']
    children_model_classes = clone(BroadlinkDeviceModel.children_model_classes)
    children_model_classes |= { 'state': { 'class': TvStateModel } }
    children_model_classes['collection_ref']['attrs'] = collection
