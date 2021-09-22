from .device_controller import DeviceController
from ..models import PingableDevicesModel
import os


class PingableDeviceController(DeviceController):
    model_class = PingableDevicesModel


    def get_power(self):
        ping = self.model.power_by_ping
        if self.model.addr and ping:
            addr = self.model.addr
            return 'off' if os.system(f'fping -c1 -t100 {addr} &>/dev/null') else 'on'
        return super().get_power()
