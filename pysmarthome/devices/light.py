from .device import Device

class Light(Device):
    def __init__(self, color='#ffffff', brightness=100, **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.brightness = brightness


    def set_rgb_color(self, rgb):
        pass


    def set_brightness(self):
        pass
