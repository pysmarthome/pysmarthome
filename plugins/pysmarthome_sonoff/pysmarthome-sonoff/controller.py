import sonoffreq
from pysmarthome import DeviceController, DevicesModel

class SonoffDeviceController(DeviceController):
    model_class = DevicesModel.clone('SonoffsModel')
    model_class.schema |= {
        'addr': { 'type': 'string' },
        'api_key': { 'type': 'string' },
    }


    def on_load(self, addr='', api_key='', **data):
        self.dev = sonoffreq.Sonoff(addr, api_key)


    def on(self):
        self.dev.switch('on')
        return True


    def off(self):
        self.dev.switch('off')
        return True
