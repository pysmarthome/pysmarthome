from .device_model import DevicesModel, DeviceStatesModel, SnapshotStatesModel
from durc import clone


class AcStatesModel(DeviceStatesModel):
    schema = clone(DeviceStatesModel.schema) | {
        'temp': { 'type': 'integer', 'default': 16 },
    }
    collection = DeviceStatesModel.collection


class SnapshotAcStatesModel(SnapshotStatesModel):
    schema = clone(SnapshotStatesModel.schema) | {
        'temp': { 'type': 'integer' },
    }
    collection = SnapshotStatesModel.collection


    @property
    def actions(self):
        actions = super().actions
        attrs = self.attrs
        if 'temp' in attrs:
            actions.append(('set_temp_to', self.temp))
        return actions


class AcsModel(DevicesModel):
    schema = clone(DevicesModel.schema) | {
        'temp_max': { 'type': 'integer', 'default': 24 },
        'temp_min': { 'type': 'integer', 'default': 16 },
    }
    children_model_classes = clone(DevicesModel.children_model_classes)
    children_model_classes['state']['class'] = AcStatesModel
    children_model_classes['snapshot_states']['class'] = SnapshotAcStatesModel
