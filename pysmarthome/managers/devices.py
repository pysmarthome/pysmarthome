from ..devices import Tv, Ac, FloorLamp, BroadlinkDevice
from ..devices import GoveeLedStrip
from ..devices import Yeelight
from ..devices import SonoffDevice
from ..devices import Pc

from .broadlink import BroadlinkManager
from .govee import GoveeManager


class DevicesManager:
    controllers = {
        'broadlink': BroadlinkDevice,
        'tv': Tv,
        'ac': Ac,
        'broadlink_rgb_lamp': FloorLamp,
        'yeelight': Yeelight,
        'sonoff': SonoffDevice,
        'pc': Pc,
        'govee': GoveeLedStrip,
    }
    controller_apis_cls = {
        'govee': GoveeManager,
        'broadlink': BroadlinkManager,
    }
    ref_ids = {}


    def __init__(self, db):
        self.db = db
        self.devices = {}
        self.controller_apis = {}
        self.load_controllers()


    def load_controllers(self):
        for data in self.db.collections['api_configs'].documents:
            id = data['id']
            name = data['name']
            self.load_controller(id, name)


    def load_controller(self, id, controller_id):
        ctrl_class = DevicesManager.controller_apis_cls[controller_id]
        ctrl = ctrl_class.load(self.db, id)
        self.add_controller(ctrl)
        return ctrl


    def load_devices(self):
        for doc in self.db.collections['devices'].documents:
            id = doc['id']
            c_id = doc['controller']
            self.load_device(id, c_id)


    def load_device(self, id, controller_id):
        controller_class = DevicesManager.controllers[controller_id]
        device = controller_class.load(self.db, id, self.on_dev_loaded)
        self.add_device(device)
        return device


    def on_dev_loaded(self, dev):
        ctrl = self.get_controller(dev.controller_api)
        if ctrl:
            ctrl.add_device(dev)


    def create_device(self, **data):
        pass


    def add_device(self, dev):
        self.devices[dev.id] = dev
        self.ref_ids[dev.name] = dev.id


    def add_controller(self, ctrl):
        self.controller_apis[ctrl.name] = ctrl


    def get_device(self, id='', name=''):
        if name and name in self.ref_ids:
            return self.devices[self.ref_ids[name]]
        if id in self.devices:
            return self.devices[id]
        return None


    def get_controller(self, id):
        if id in self.controller_apis_cls:
            return self.controller_apis[id]
        return None


    def get_devices(self, cls=None):
        devices = self.devices.values()
        if cls != None:
            return filter(lambda d: isinstance(d, cls), devices)
        return devices


    def get_controllers(self):
        return list(self.controller_apis.values())
