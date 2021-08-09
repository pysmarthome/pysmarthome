from flask_restful import Api
from .resources import LavaLampResource, SaltLampResource
from .resources import FloorLampResource, AcResource, TvResource
from .resources import PCLampResource
from .resources import LedStripResource
from .resources import PCResource
from .resources import LightsResource
from .devices import GoveeLedStrip, Light


def register_endpoints(app, devices_manager):
    api = Api(app)

    # pc
    api.add_resource(
        PCResource,
        '/pc', '/pc/<device>', '/pc/<device>/<id>',
        resource_class_args=[devices_manager.get_device('pc')],
    )

    # pc lamp
    api.add_resource(
        PCLampResource,
        '/pc_lamp',
        resource_class_args=[devices_manager.get_device('pc_lamp')]
    )

    # lava lamp
    api.add_resource(
        LavaLampResource,
        '/lava_lamp',
        resource_class_args=[devices_manager.get_device('lava_lamp')]
    )

    # salt lamp
    api.add_resource(
        SaltLampResource,
        '/salt_lamp',
        resource_class_args=[devices_manager.get_device('salt_lamp')]
    )

    # ac
    api.add_resource(
        AcResource,
        '/ac',
        resource_class_args=[devices_manager.get_device('ac')]
    )

    # tv
    api.add_resource(
        TvResource,
        '/tv',
        resource_class_args=[devices_manager.get_device('tv')]
    )

    # floor_lamp
    api.add_resource(
        FloorLampResource,
        '/floor_lamp',
        resource_class_args=[devices_manager.get_device('floor_lamp')]
    )

    # Led strips
    led_strips = devices_manager.get_devices(cls=GoveeLedStrip)
    led_strip_devs = dict(map(lambda d: (d.get_id(), d), led_strips))
    api.add_resource(
        LedStripResource,
        '/led_strip/<id>',
        resource_class_args=[led_strip_devs],
    )

    # Lights
    api.add_resource(
        LightsResource,
        '/lights',
        resource_class_kwargs={
            'devices': list(devices_manager.get_devices(cls=Light)),
        }
    )

    return api
