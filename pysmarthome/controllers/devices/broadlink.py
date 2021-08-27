from .device import Device
from pysmarthome.models import BroadlinkDeviceModel
from pysmarthome.managers.broadlink import BroadlinkManager


class BroadlinkDevice(Device):
    model_class = BroadlinkDeviceModel
    manager_class = BroadlinkManager


    def get_command_data(self, id):
        return self.model.commands.get(id)


    def send_command(self, id):
        self.dev.send_data(self.get_command_data(id))


    def set_command(self, id, data):
        self.dev.model.commands.set(id, data)
