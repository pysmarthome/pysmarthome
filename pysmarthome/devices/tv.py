from .broadlink import BroadlinkDevice
import os
from pysmarthome.models import TvModel
from pysmarthome.config import ping_cmd

class Tv(BroadlinkDevice):
    model_class = TvModel

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


    def vol_up(self):
        if self.model.state.volume < 100:
            self.send_command('vol_up')
            self.set_state(volume=self.model.state.volume + 1)
            return True
        return False


    def vol_down(self):
        if self.model.state.volume > 0:
            self.send_command('vol_down')
            self.set_state(volume=self.model.state.volume - 1)
            return True
        return False


    def get_power(self):
        addr = self.model.addr
        return 'off' if os.system(f'{ping_cmd} {addr} &>/dev/null') else 'on'
