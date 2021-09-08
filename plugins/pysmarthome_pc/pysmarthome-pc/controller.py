from pysmarthome import DeviceController
import wakeonlan
import requests
import json
import os
from .model import PcsModel


class PcController(DeviceController):
    model_class = PcsModel


    def on(self):
        wakeonlan.send_magic_packet(self.model.mac_addr)


    def off(self):
        self.dispatch('off')


    def get_power(self):
        ping_cmd = self.model.ping_cmd
        if ping_cmd:
            addr = self.model.addr
            return 'off' if os.system(f'{ping_cmd} {addr} &>/dev/null') else 'on'
        return super().get_power()


    def dispatch(self, action_id=''):
        action = self.model.actions.get(action_id)

        addr = self.model.actions_handler['addr']
        path = action['path']
        api_key = self.model.actions_handler['api_key']
        data = action['data']

        return requests.post(
            f'http://{addr}/{path}',
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json',
                'API_KEY': api_key,
            },
            data=data,
        )
