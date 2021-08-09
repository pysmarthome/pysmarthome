import sonoffreq
from .device import Device


class SonoffDevice(Device):
    def __init__(self, addr, api_key, **kwargs):
        super().__init__(**kwargs)
        self.dev = sonoffreq.Sonoff(addr, api_key)


    def on(self):
        self.dev.switch('on')
        return True


    def off(self):
        self.dev.switch('off')
        return True
