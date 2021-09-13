from abc import ABC, abstractmethod
from .device_controller import DeviceController
from ..models import RgbLampsModel


class RgbLampController(DeviceController, ABC):
    model_class = RgbLampsModel


    def get_color(self):
        return self.model.state.color


    def get_brightness(self):
        return self.model.state.brightness


    @abstractmethod
    def set_color(self, rgb):
        pass


    @abstractmethod
    def set_brightness(self, val):
        pass
