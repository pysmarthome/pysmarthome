from .light import Light

class GoveeLedStrip(Light):
    def __init__(self, dev, **kwargs):
        super().__init__(**kwargs)
        self.dev = dev
        self.color = self.get_color()
        self.brightness = self.get_brightness()
        self.power = self.get_power()


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
