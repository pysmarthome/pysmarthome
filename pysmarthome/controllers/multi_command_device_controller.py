from abc import abstractmethod
from ..models import MultiCommandDevicesModel
from .device_controller import DeviceController

class MultiCommandDeviceController(DeviceController):
    model_class = MultiCommandDevicesModel


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True


    @abstractmethod
    def send_command(self, id):
        pass


    def add_command(self, id, data):
        pass


    def remove_command(self, id):
        pass


    def update_command(self, id, data):
        pass


    def set_int_state_attr_to(self, attr, f):
        self.set_int_state_attr_by(attr, int(f) - getattr(self.model.state, attr))


    def set_int_state_attr_by(self, attr, n=0, delta=0):
        curr_val = getattr(self.model.state, attr) + delta
        max_val = int(getattr(self.model, f'{attr}_max'))
        min_val = int(getattr(self.model, f'{attr}_min'))
        n = int(n)
        if (n > 0 and curr_val < max_val) or (n < 0 and curr_val > min_val):
            cmd = f'{attr}_up' if n > 0 else f'{attr}_down'
            self.send_command(cmd)
            inc = 1 if n > 0 else -1
            self.set_int_state_attr_by(attr, n - inc, delta + inc)
            return True
        if delta:
            self.set_state(**{attr: curr_val})
        return False
