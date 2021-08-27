from .model import Model, clone
from .refs import ManagerConfigsRefModel
from pysmarthome.config import collections

class ManagerConfigsModel(Model):
    schema = clone(Model.schema)
    children_model_classes = {
        'ref': { 'class': ManagerConfigsRefModel }
    }


class GoveeConfigModel(ManagerConfigsModel):
    schema = clone(ManagerConfigsModel.schema)
    schema |= {
        'email': { 'type': 'string', 'required': True },
        'password': { 'type': 'string', 'required': True }
    }
    collection = collections['govee_config']


class BroadlinkConfigModel(ManagerConfigsModel):
    schema = clone(ManagerConfigsModel.schema)
    schema |= { 'addr': { 'type': 'string', 'required': True } }
    collection = collections['broadlink_config']
