from govee_api2 import api
from pysmarthome import Manager


class GoveeManager(Manager):
    ref_ids = {}


    @classmethod
    def init_client(cls, email='', password='', **config):
        i = cls.instance
        print('Login on govee API')
        i.client = api.Govee(email, password)
        i.client.login()
        i.client.on_device_update = i.on_device_update
        i.client.update_device_list()


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
        self.ref_ids[device.model.mac_addr] = device.id
        device.dev = self.get_client_device(device.model.mac_addr)


    def get_client_device(self, id):
        if id in self.client.devices:
            return self.client.devices[id]
        return None
