from pysmarthome.models.refs import ManagerConfigsRefModel
from pysmarthome.config import collections
from pysmarthome.models import GoveeConfigModel, BroadlinkConfigModel
from pysmarthome.managers import BroadlinkManager, GoveeManager


class ManagersFactory:
    collections_map = {
        collections['broadlink_config']: {
            'model': BroadlinkConfigModel,
            'manager': BroadlinkManager,
        },
        collections['govee_config']: {
            'model': GoveeConfigModel,
            'manager': GoveeManager,
        },
    }


    @staticmethod
    def init_all(db):
        models = ManagersFactory.load_all(db)
        for m in models:
            c_id = m.collection
            if c_id in ManagersFactory.collections_map:
                manager = ManagersFactory.collections_map[c_id]['manager']
                manager.init_client(**m.to_dict())


    @staticmethod
    def load_all(db):
        models = ManagerConfigsRefModel.load_all(db)
        configs = []
        for m in models:
            c_id = m.collection_id
            if c_id in ManagersFactory.collections_map:
                config_model_cls = ManagersFactory.collections_map[c_id]['model']
                config_model = config_model_cls.load_one(db)
                configs.append(config_model)
        return configs
