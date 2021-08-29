from .manager import GoveeManager
from .controller import GoveeLedStripController

config = {
    'email': { 'type': 'string', 'required': True },
    'password': { 'type': 'string', 'required': True }
}

device_controllers = [ GoveeLedStripController ]


def on_load(**data):
    GoveeManager.init_client(**data)
