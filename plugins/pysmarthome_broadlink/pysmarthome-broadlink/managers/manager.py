import broadlink
from pysmarthome import Manager


class BroadlinkManager(Manager):
    @classmethod
    def init_client(cls, addr='', **config):
        print('Syncing with broadlink')
        i = cls.instance
        i.client = broadlink.discover(
            timeout=2,
            discover_ip_address=addr,
        )[0]
        i.client.auth()
        print('Auth!')


    def on_device_added(self, device):
        device.dev = self.client


    def send_data(self, data):
        self.client.send_data(data)
