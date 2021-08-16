from .light import Light
from pysmarthome.models import RgbLightModel


class GoveeLedStrip(Light):
    model_class = RgbLightModel
    controller_api = 'govee'


    def on(self):
        if self.should_update_power('on'):
            self.dev.on = True
            return True
        return False


    def off(self):
        if self.should_update_power('off'):
            self.dev.on = False
            return True
        return False


    def toggle(self):
        self.dev.toggle()
        return True


    def get_color(self):
        return self.dev.color


    def get_brightness(self):
        return self.dev.brightness


    def get_power(self):
        return 'on' if self.dev.on else 'off'


    def is_on(self):
        return self.dev.on
