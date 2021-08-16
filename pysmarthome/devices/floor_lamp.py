from .light import Light
from .broadlink import BroadlinkDevice
from pysmarthome.models import BroadlinkRgbLightModel

class FloorLamp(BroadlinkDevice, Light):
    model_class = BroadlinkRgbLightModel


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True
