class DevicesManager:
    def __init__(self):
        self.devices = {}


    def add_device(self, dev):
        id = dev.get_id()
        self.devices[id] = dev


    def get_device(self, id):
        if id in self.devices:
            return self.devices[id]
        return None


    def get_devices(self, cls=None):
        devices = self.devices.values()
        if cls != None:
            return filter(lambda d: isinstance(d, cls), devices)
        return devices
