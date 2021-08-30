from flask_restful import Api
from .resources.devices import DevicesResource
from .resources.states import StatesResource


def register_endpoints(app):
    api = Api(app)

    # devices
    api.add_resource(
        DevicesResource,
        '/', '/<id>',
    )

    # states
    api.add_resource(
        StatesResource,
        '/states', '/states/<id>',
    )
    return api
