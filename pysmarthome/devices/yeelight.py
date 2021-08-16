from .light import Light
import yeelight
from pysmarthome.models import RgbLightModel

class Yeelight(Light):
    model_class = RgbLightModel


    def on_load(self, addr='', **data):
        self.dev = yeelight.Bulb(addr)
        super().on_load(**data)


    def on(self):
        return True if self.dev.turn_on() == 'ok' else False


    def off(self):
        return True if self.dev.turn_off() == 'ok' else False


    def toggle(self):
        return True if self.dev.toggle() == 'ok' else False


    def get_brightness(self):
        properties = self.dev.get_properties()
        return properties['current_brightness']


    def set_brightness(self):
        pass


    def set_color(self):
        pass


    def get_color(self):
        properties = self.dev.get_properties()
        rgb = properties['rgb']
        return f'#{rgb}'


    def get_power(self):
        properties = self.dev.get_properties()
        return properties['power']
