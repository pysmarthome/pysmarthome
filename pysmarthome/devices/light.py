from abc import ABC, abstractmethod
from .device import Device

class Light(Device, ABC):
    def get_color(self):
        return self.model.state.color


    def get_brightness(self):
        return self.model.state.brightness


    @abstractmethod
    def set_color(self, rgb):
        pass


    @abstractmethod
    def set_brightness(self):
        pass
