from .light import Light
import yeelight


class Yeelight(Light):
    def __init__(self, addr, **kwargs):
        super().__init__(**kwargs)
        self.dev = yeelight.Bulb(addr)
        self.power = self.get_power()
        self.color = self.get_color()
        self.brightness = self.get_brightness()


    def on(self):
        return True if self.dev.turn_on() == 'ok' else False


    def off(self):
        return True if self.dev.turn_off() == 'ok' else False


    def toggle(self):
        return True if self.dev.toggle() == 'ok' else False


    def get_brightness(self):
        properties = self.dev.get_properties()
        return properties['current_brightness']


    def get_color(self):
        properties = self.dev.get_properties()
        rgb = properties['rgb']
        return f'#{rgb}'


    def get_power(self):
        properties = self.dev.get_properties()
        return properties['power']
