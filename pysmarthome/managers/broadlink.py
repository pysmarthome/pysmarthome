import broadlink

class BroadlinkManager:
    def __init__(self, addr):
        self.client = broadlink.discover(
            timeout=2,
            discover_ip_address=addr,
        )[0]
        self.client.auth()


    def send_data(self, data):
        self.client.send_data(data)
