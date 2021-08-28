from pysmarthome.config import collections
from vesla_pymvc import Model


class RefModel(Model):
    schema = {
        **Model.schema,
        'collection_id': {
            'type': 'string',
            'required': True,
        }
    }


class DevicesRefModel(RefModel):
    collection = collections['devices_ref']


class ManagerConfigsRefModel(RefModel):
    collection = collections['configs_ref']
