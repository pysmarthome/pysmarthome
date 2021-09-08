from ariadne import InterfaceType

device = InterfaceType('Device')

@device.type_resolver
def resolve_device_type(obj, *_):
    return obj['typename']


state = InterfaceType('BaseState')
@state.type_resolver
def resolve_state_type(obj, *_):
    return obj['typename']
