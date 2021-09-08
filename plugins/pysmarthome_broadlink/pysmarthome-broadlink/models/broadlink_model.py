import base64
from durc import Model, clone
from pysmarthome import DevicesModel

class BroadlinkCommandsModel(Model):
    schema = {
        **Model.schema,
        'name': { 'type': 'string' },
        'data': { 'type': 'string' },
        'label': { 'type': 'string', 'default': '' },
    }


    @property
    def decoded(self): return base64.b64decode(self.data)


class BroadlinkDevicesModel(DevicesModel):
    children_model_classes = clone(DevicesModel.children_model_classes) | {
        'commands': { 'class': BroadlinkCommandsModel, 'quantity': '*' },
    }
