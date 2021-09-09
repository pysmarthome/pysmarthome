from abc import abstractmethod
from ..models import AcsModel
from .device_controller import DeviceController

class AcController(DeviceController):
    model_class = AcsModel


    @abstractmethod
    def set_temp_by(self, n):
        pass


    @abstractmethod
    def set_temp_to(self, target):
        pass
