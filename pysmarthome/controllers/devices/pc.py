import wakeonlan
import requests
import json
from .device import Device
import os
from pysmarthome.models import PcModel
from pysmarthome.config import ping_cmd

class Pc(Device):
    model_class = PcModel


    def on(self):
        wakeonlan.send_magic_packet(self.model.mac_addr)


    def off(self):
        self.dispatch('off')


    def get_power(self):
        addr = self.model.addr
        return 'off' if os.system(f'{ping_cmd} {addr} &>/dev/null') else 'on'


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
