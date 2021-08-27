from pysmarthome.config import collections
from .device_model import DeviceStateModel, DeviceModel
from .device_model import clone
from .broadlink_model import BroadlinkDeviceModel


class AcStateModel(DeviceStateModel):
    schema = clone(DeviceStateModel.schema)
    schema['state']['schema'] |= {
        'temp': { 'type': 'integer', 'min': 16, 'max': 24, 'default': 16 },
    }


class AcModel(BroadlinkDeviceModel):
    schema = clone(BroadlinkDeviceModel.schema)
    collection = collections['acs']
    children_model_classes = clone(BroadlinkDeviceModel.children_model_classes)
    children_model_classes |= { 'state': { 'class': AcStateModel } }
