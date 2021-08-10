from .broadlink import BroadlinkDevice
import os


class Tv(BroadlinkDevice):
    def __init__(self, manager, volume=0, addr='', is_muted=False, **kwargs):
        super().__init__(manager, **kwargs)
        self.is_muted = False
        self.volume = volume
        self.addr = addr
        self.power = self.get_init_power()


    def on(self):
        if self.should_update_power('on'):
            self.send_data(self.commands['toggle'])
            return True
        return False


    def off(self):
        if self.should_update_power('off'):
            self.send_data(self.commands['toggle'])
            return True
        return False


    def toggle(self):
        self.send_data(self.commands['toggle'])
        return True


    def mute(self):
        self.send_data(self.commands['mute'])
        self.is_muted = not self.is_muted


    def vol_up(self):
        self.send_data(self.commands['vol_up'])
        self.volume += 1


    def vol_down(self):
        self.send_data(self.commands['vol_up'])
        self.volume -= 1


    def get_init_power(self):
        return 'off' if os.system(f'ping -w 1 {self.addr} &>/dev/null') else 'on'
