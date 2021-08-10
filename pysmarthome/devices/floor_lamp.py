from .light import Light
from .broadlink import BroadlinkDevice

class FloorLamp(BroadlinkDevice, Light):
    def __init__(self, manager, commands={}, **kwargs):
        BroadlinkDevice.__init__(self, manager, commands)
        Light.__init__(self, **kwargs)


    def on(self):
        self.send_data(self.commands['on'])
        return True


    def off(self):
        self.send_data(self.commands['off'])
        return True
