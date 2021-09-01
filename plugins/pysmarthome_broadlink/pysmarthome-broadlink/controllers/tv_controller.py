from .broadlink_controller import BroadlinkDeviceController
import os
from ..models import TvsModel

class TvController(BroadlinkDeviceController):
    model_class = TvsModel


    def on(self):
        if self.should_update_power('on'):
            self.send_command('toggle')
            return True
        return False


    def off(self):
        if self.should_update_power('off'):
            self.send_command('toggle')
            return True
        return False


    def toggle(self):
        self.send_command('toggle')
        return True


    def mute(self):
        self.send_command('mute')
        self.set_state(mute=not self.model.state.mute)


    def vol_to(self, f):
        self.vol(int(f) - self.model.state.volume)


    def vol(self, n=0, delta=0):
        curr_vol = self.model.state.volume + delta
        n = int(n)
        if (n > 0 and curr_vol < 100) or (n < 0 and curr_vol > 0):
            cmd = 'vol_up' if n > 0 else 'vol_down'
            self.send_command(cmd)
            inc = 1 if n > 0 else -1
            self.vol(n - inc, delta + inc)
            return True
        if delta:
            self.set_state(volume=curr_vol)
        return False


    def get_power(self):
        ping_cmd = self.model.ping_cmd
        if ping_cmd:
            addr = self.model.addr
            return 'off' if os.system(f'{ping_cmd} {addr} &>/dev/null') else 'on'
        return super().get_power()
