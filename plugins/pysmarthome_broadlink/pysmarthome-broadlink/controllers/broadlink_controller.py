from pysmarthome_lib import DeviceController
from ..models import BroadlinkDevicesModel
from ..managers.manager import BroadlinkManager


class BroadlinkDeviceController(DeviceController):
    model_class = BroadlinkDevicesModel
    manager_class = BroadlinkManager


    def get_command_data(self, id):
        return self.model.commands.get(id)


    def send_command(self, id):
        self.dev.send_data(self.get_command_data(id))


    def set_command(self, id, data):
        self.dev.model.commands.set(id, data)
