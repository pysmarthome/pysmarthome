from pysmarthome import DeviceController
from ..models import BroadlinkDevicesModel
from ..managers.manager import BroadlinkManager


class BroadlinkDeviceController(DeviceController):
    model_class = BroadlinkDevicesModel
    manager_class = BroadlinkManager


    def send_command(self, id):
        for cmd in self.model.commands:
            if (cmd.label == id) or (cmd.id == id):
                return self.dev.send_data(cmd.decoded)


    def set_command(self, id, data):
        self.dev.model.commands.set(id, data)
