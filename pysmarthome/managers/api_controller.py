from abc import ABC, abstractmethod
from ..models import ApiConfigModel

class ApiController(ABC):
    def __init__(self):
        self._client = None
        self.devices = {}
        self.model = ApiConfigModel()


    @property
    def name(self): return self.model.name


    @property
    def client(self):
        if not self._client: self.init_client(**self.model.attrs)
        return self._client


    @client.setter
    def client(self, c): self._client = c


    @classmethod
    def load(cls, db, id):
        c = cls()
        c.model = ApiConfigModel.load(db, id)
        return c

    @abstractmethod
    def init_client(self, **config):
        pass


    @abstractmethod
    def on_device_added(self, device):
        pass


    def add_device(self, device):
        self.devices[device.id] = device
        self.on_device_added(device)


    def get_device(self, id):
        if id in self.devices:
            return self.devices[id]
        return None
