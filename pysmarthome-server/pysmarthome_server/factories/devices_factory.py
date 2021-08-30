from pysmarthome_lib import DevicesModel


class DevicesFactory:
    collections_map = {}

    @staticmethod
    def init(plugins):
        for plugin in plugins:
            controller_classes = plugin.device_controllers
            for v in controller_classes:
                k = v.model_class.collection
                DevicesFactory.collections_map[k] = v


    @staticmethod
    def load(db, id):
        try:
            refs = DevicesModel.children_model_classes['collection_ref']['class']
            c_id = refs.load(db, id).collection_id
            dev_cls = DevicesFactory.collections_map[c_id]
            return dev_cls.load(db, id)
        except Exception as e:
            raise e


    @staticmethod
    def load_all(db):
        devs = []
        refs = DevicesModel.children_model_classes['collection_ref']['class']
        ids = [ m.id for m in refs.load_all(db) ]
        for id in ids:
            devs.append(DevicesFactory.load(db, id))
        return devs
