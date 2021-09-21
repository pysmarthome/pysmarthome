from .device_model import DevicesModel, DeviceStatesModel, SnapshotStatesModel
from durc import clone


class RgbLampStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'color': { 'type': 'string', 'default': '#ffffff' },
        'brightness': { 'type': 'number', 'default': 0 },
    }
    collection = DeviceStatesModel.collection


class SnapshotRgbLampStatesModel(SnapshotStatesModel):
    schema = clone(SnapshotStatesModel.schema) | {
        'color': { 'type': 'string' },
        'brightness': { 'type': 'number' },
    }
    collection = SnapshotStatesModel.collection


    @property
    def actions(self):
        actions = super().actions
        attrs = self.attrs
        if 'color' in attrs:
            actions.append(('set_color', self.color))
        if 'brightness' in attrs:
            actions.append(('set_brightness', self.brightness))
        return actions


class RgbLampsModel(DevicesModel):
    schema = clone(DevicesModel.schema)
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes['state']['class'] = RgbLampStatesModel
    children_model_classes['snapshot_states']['class'] = SnapshotRgbLampStatesModel
