from .broadlink import BroadlinkDevice
from pysmarthome.models import AcModel

class Ac(BroadlinkDevice):
    model_class = AcModel


    def on(self):
        if self.should_update_power('on'):
            self.send_command('on')
            return True
        return False


    def off(self):
        if self.should_update_power('off'):
            self.send_command('off')
            return True
        return False
