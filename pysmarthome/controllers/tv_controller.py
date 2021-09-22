from abc import abstractmethod
from ..models import TvsModel
from .pingable_device_controller import PingableDeviceController

class TvController(PingableDeviceController):
    model_class = TvsModel


    @abstractmethod
    def mute(self):
        pass


    @abstractmethod
    def set_vol_by(self, n):
        pass


    @abstractmethod
    def set_vol_to(self, target):
        pass
