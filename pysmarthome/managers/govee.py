from govee_api2 import api

class GoveeManager:
    def __init__(self, username, password):
        self.client = api.Govee(username, password)
        self.client.login()
        self.client.on_device_update = self.on_device_update
        self.client.update_device_list()
        self.devices = {}
        self.id_refs = {}


    def on_device_update(self, client, client_dev, raw_data):
        id_ref = self.id_refs[client_dev.identifier]
        dev = self.devices[id_ref]
        state = raw_data['state']
        c = state['color']
        dev.set_state({
            'power': 'on' if state['onOff'] else 'off',
            'brightness': round(100 * (state['brightness'] / 255)),
            'color': '#{:02x}{:02x}{:02x}'.format(c['r'], c['g'], c['b']),
        })


    def add_device(self, device):
        id = device.get_id()
        self.id_refs[device.dev.identifier] = id
        self.devices[id] = device


    def get_client_devices(self):
        return self.client.devices.values()
