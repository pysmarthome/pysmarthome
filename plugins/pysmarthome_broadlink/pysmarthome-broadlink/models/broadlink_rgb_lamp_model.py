from pysmarthome import RgbLampsModel, RgbLampStatesModel, clone
from .broadlink_model import BroadlinkDevicesModel, BroadlinkCommandsModel


class BroadlinkRgbLampsModel(BroadlinkDevicesModel, RgbLampsModel):
    schema = clone(RgbLampsModel.schema) | clone(BroadlinkDevicesModel.schema)
    children_model_classes = clone(BroadlinkDevicesModel.children_model_classes)
    children_model_classes['state']['class'] = RgbLampStatesModel
