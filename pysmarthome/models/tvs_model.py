from .device_model import PingableDevicesModel, DeviceStatesModel, SnapshotStatesModel
from durc import clone


class TvStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100, 'default': 0 },
        'mute': { 'type': 'boolean', 'default': False },
    }
    collection = DeviceStatesModel.collection


class SnapshotTvStatesModel(SnapshotStatesModel):
    schema = clone(SnapshotStatesModel.schema) | {
        'volume': { 'type': 'integer', 'min': 0, 'max': 100 },
        'mute': { 'type': 'boolean' },
    }
    collection = SnapshotStatesModel.collection


    @property
    def actions(self):
        actions = super().actions
        attrs = self.attrs
        if 'volume' in attrs:
            actions.append(('set_vol_to', self.volume))
        if 'mute' in attrs:
            actions.append(('mute', self.mute))
        return actions


class TvsModel(PingableDevicesModel):
    schema = clone(PingableDevicesModel.schema) | {
        'volume_max': { 'type': 'integer', 'default': 100 },
        'volume_min': { 'type': 'integer', 'default': 0 },
    }
    children_model_classes = clone(PingableDevicesModel.children_model_classes)
    children_model_classes['state']['class'] = TvStatesModel
    children_model_classes['snapshot_states']['class'] = SnapshotTvStatesModel
