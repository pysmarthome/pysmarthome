from .broadlink import BroadlinkDevice


class Ac(BroadlinkDevice):
    def __init__(self, manager, temp=0, **kwargs):
        super().__init__(manager, **kwargs)
        self.temp = temp


    def on(self):
        if self.should_update_power('on'):
            self.send_data(self.commands['on'])
            return True
        return False


    def off(self):
        if self.should_update_power('off'):
            self.send_data(self.commands['off'])
            return True
        return False
