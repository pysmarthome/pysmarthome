from abc import abstractmethod
from ..models import TvsModel
from .device_controller import DeviceController

class TvController(DeviceController):
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
