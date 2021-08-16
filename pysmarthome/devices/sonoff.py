import sonoffreq
from .device import Device


class SonoffDevice(Device):
    def on_load(self, addr='', api_key='', **data):
        self.dev = sonoffreq.Sonoff(addr, api_key)

    def on(self):
        self.dev.switch('on')
        return True


    def off(self):
        self.dev.switch('off')
        return True
