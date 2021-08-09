import wakeonlan
import requests
import json
from .device import Device
import os

class Pc(Device):
    def __init__(self, actions_handler_addr='', actions_handler_api_key='',
            addr='', mac_addr='', **kwargs):
        super().__init__(**kwargs)
        self.subdev_actions_map = {
            'player': ['play', 'pause', 'next', 'previous'],
            'audio': ['tv', 'phone'],
            'display': ['plug', 'unplug'],
        }
        self.addr = addr
        self.mac_addr = mac_addr
        self.actions_handler_addr = actions_handler_addr
        self.actions_handler_api_key = actions_handler_api_key


    def on(self):
        wakeonlan.send_magic_packet(self.mac_addr)


    def off(self):
        self.actions_handler_dispatch('off')


    def get_power(self):
        return 'off' if os.system(f'ping -w 1 {self.addr} &>/dev/null') else 'on'


    def actions_handler_dispatch(self, action, path=''):
        addr = self.actions_handler_addr
        api_key = self.actions_handler_api_key

        return requests.post(
            f'http://{addr}/{path}',
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Accept': 'application/json',
                'API_KEY': api_key,
            },
            data=json.dumps({
                'action': action,
            })
        )


    def trigger_action(self, action_id, sub_dev_id='', id=''):
        if sub_dev_id in self.subdev_actions_map:
            path = sub_dev_id if id == '' else f'{sub_dev_id}/{id}'
            return self.actions_handler_dispatch(action_id, path)
        return super().trigger_action(action_id)
