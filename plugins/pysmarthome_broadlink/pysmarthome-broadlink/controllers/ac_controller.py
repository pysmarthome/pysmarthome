from .broadlink_controller import BroadlinkDeviceController
from ..models import AcsModel

class AcController(BroadlinkDeviceController):
    model_class = AcsModel


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
