from govee_api2 import api
from .api_controller import ApiController


class GoveeManager(ApiController):
    ref_ids = {}

    def init_client(self, email='', password='', **config):
        print('Login on govee API')
        self._client = api.Govee(email, password)
        self._client.login()
        self._client.on_device_update = self.on_device_update
        self._client.update_device_list()


    def on_device_update(self, client, client_dev, raw_data):
        id = client_dev.identifier
        if id not in self.ref_ids: return

        ref_id = self.ref_ids[id]
        dev = self.get_device(ref_id)
        state = raw_data['state']

        power = 'on' if state['onOff'] else 'off'
        brightness = round(100 * (state['brightness'] / 255))
        c = state['color']
        color = '#{:02x}{:02x}{:02x}'.format(c['r'], c['g'], c['b'])

        print(f'Lets try to update the state of {dev.name}')
        print(f'power: {power} | brightness: {brightness} | color {color}.')

        try:
            dev.set_state(power=power, brightness=brightness, color=color)
        except Exception as e:
            print(e)


    def on_device_added(self, device):
        self.ref_ids[device.mac_addr] = device.id
        device.dev = self.get_client_device(device.mac_addr)


    def get_client_device(self, id):
        if id in self.client.devices:
            return self.client.devices[id]
        return None


    def get_client_devices(self):
        return self.client.devices
