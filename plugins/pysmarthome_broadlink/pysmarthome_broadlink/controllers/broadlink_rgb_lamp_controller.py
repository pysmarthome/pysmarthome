from pysmarthome_lib import RgbLampController
from .broadlink_controller import BroadlinkDeviceController
from ..models import BroadlinkRgbLampsModel

class BroadlinkRgbLampController(BroadlinkDeviceController, RgbLampController):
    model_class = BroadlinkRgbLampsModel


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True


    def set_brightness(self):
        pass


    def set_color(self, color_id):
        self.send_command(color_id)
        color = self.model.commands.hex(color_id)
        self.set_state(color=color)
        return True


    def available_colors(self):
        return self.model.commands.colors()
