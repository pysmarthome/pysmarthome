from .model import Model, clone
from pysmarthome.config import collections

class ManagerConfigsModel(Model):
    schema = clone(Model.schema)


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
