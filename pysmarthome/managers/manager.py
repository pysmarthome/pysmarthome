from abc import ABC, abstractmethod

class Manager(ABC):
    _instance = None


    def __init__(self):
        self._client = None
        self.devices = {}


    @classmethod
    @property
    def instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


    @property
    def client(self): return self._client


    @client.setter
    def client(self, c): self._client = c


    @classmethod
    @abstractmethod
    def init_client(self, **config):
        pass


    @abstractmethod
    def on_device_added(self, device):
        pass


    @classmethod
    def add_device(cls, device):
        i = cls.instance
        i.devices[device.id] = device
        i.on_device_added(device)


    def get_device(self, id):
        if id in self.devices:
            return self.devices[id]
        return None
