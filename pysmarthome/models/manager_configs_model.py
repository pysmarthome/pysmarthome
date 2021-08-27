from .model import Model, clone
from pysmarthome.config import collections

class ManagerConfigsModel(Model):
    schema = clone(Model.schema)


class BroadlinkConfigModel(ManagerConfigsModel):
    schema = clone(ManagerConfigsModel.schema)
    schema |= { 'addr': { 'type': 'string', 'required': True } }
    collection = collections['broadlink_config']
