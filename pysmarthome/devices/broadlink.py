from .device import Device

class BroadlinkDevice(Device):
    def __init__(self, manager, commands = {}, **kwargs):
        super().__init__(**kwargs)
        self.manager = manager
        self.commands = commands


    def send_data(self, data):
        self.manager.send_data(data)


    def set_command(self, id, data):
        self.commands[id] = data
