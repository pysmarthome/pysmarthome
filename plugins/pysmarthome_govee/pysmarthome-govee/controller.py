from pysmarthome import RgbLampController, RgbLampsModel
from .manager import GoveeManager


class GoveeLedStripController(RgbLampController):
    model_class = RgbLampsModel.clone('GoveeModel')
    model_class.schema |= {
        'mac_addr': { 'type': 'string' }
    }
    manager_class = GoveeManager


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
        return str(self.dev.color)


    def set_color(self, rgb):
        pass


    def get_brightness(self):
        try:
            return round(self.dev.brightness * 100)
        except Exception as e:
            print(e)


    def set_brightness(self):
        pass


    def get_power(self):
        return 'on' if self.dev.on else 'off'


    def is_on(self):
        return self.dev.on
