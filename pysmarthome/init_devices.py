import os

from .managers import BroadlinkManager, GoveeManager

from .devices import Tv, Ac, FloorLamp
from .devices import GoveeLedStrip
from .devices import Yeelight
from .devices import SonoffDevice
from .devices import Pc

def init_devices(devices_manager, config):
    # Broadlink
    broadlink_config = config['devices']['broadlink']
    broadlink_manager = BroadlinkManager(broadlink_config['addr'])

    # Floor Lamp
    floor_lamp = FloorLamp(
        broadlink_manager,
        id='floor_lamp',
        **broadlink_config['floor_lamp'],
    )
    devices_manager.add_device(floor_lamp)

    # Ac
    ac = Ac(
        broadlink_manager,
        id='ac',
        **broadlink_config['ac'],
    )
    devices_manager.add_device(ac)

    # Tv
    tv = Tv(
        broadlink_manager,
        id='tv',
        **broadlink_config['tv'],
    )
    devices_manager.add_device(tv)

    # Govee
    govee_config = config['devices']['govee']
    govee_manager = GoveeManager(
        username=os.getenv('GOVEE_USERNAME'),
        password=os.getenv('GOVEE_PASSWORD'),
    )
    for dev in govee_manager.get_client_devices():
        id = govee_config[dev.identifier]
        name = f'led_{id}'
        gd = GoveeLedStrip(dev, id=name)
        govee_manager.add_device(gd)
        devices_manager.add_device(gd)

    # Yeelight
    pc_lamp = Yeelight(id='pc_lamp', **config['devices']['pc_lamp'])
    devices_manager.add_device(pc_lamp)

    # Sonoff
    sonoff_devices = config['devices']['sonoff']
    for s_id, data in sonoff_devices.items():
        api_key = os.getenv(f'{s_id.upper()}_API_KEY')
        sd = SonoffDevice(api_key=api_key, id=s_id, **data)
        devices_manager.add_device(sd)

    # Pc
    pc = Pc(
        actions_handler_api_key=os.getenv('PC_ACTIONS_HANDLER_API_KEY'),
        id='pc',
        **config['devices']['pc'],
    )
    devices_manager.add_device(pc)
