from pysmarthome_lib import DeviceStatesModel, clone
from .broadlink_model import BroadlinkDevicesModel

class AcStateModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema)
    schema['state']['schema'] |= {
        'temp': { 'type': 'integer', 'min': 16, 'max': 24, 'default': 16 },
    }


class AcsModel(BroadlinkDevicesModel):
    schema = clone(BroadlinkDevicesModel.schema)
    children_model_classes = clone(BroadlinkDevicesModel.children_model_classes)
    children_model_classes |= { 'state': { 'class': AcStateModel } }
