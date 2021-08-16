import broadlink
from .api_controller import ApiController

class BroadlinkManager(ApiController):
    def init_client(self, addr='', **config):
        print('Syncing with broadlink')
        self.client = broadlink.discover(
            timeout=2,
            discover_ip_address=addr,
        )[0]
        self.client.auth()
        print('Auth!')


    def on_device_added(self, device):
        device.dev = self.client


    def send_data(self, data):
        self.client.send_data(data)
