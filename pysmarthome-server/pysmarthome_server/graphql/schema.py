from ariadne import gql, make_executable_schema
from .query_resolvers import query
from .mutation_resolvers import mutation
from .type_resolvers import device, state

type_defs = '''
    interface BaseState {
        id: ID!
        power: String!
    }

    interface Device {
        id: ID!
        name: String!
        state: BaseState!
    }

    type Plugin {
        id: ID!
        version: String
        description: String
        module_name: String!
        devices: [Device]
    }

    type DevicesInfo {
        type: String!
        ids: [ID]!
        fields: [String]
    }

    type Query {
        plugins: [Plugin!]!
        plugin(id: ID!): Plugin!
        devices(type: String, power: String): [Device]!
        device(id: ID!): Device!
        devices_info: [DevicesInfo]
    }

    type Mutation {
        toggle(id: ID!): BaseState!
        poweroff(id: ID!): BaseState!
        poweron(id: ID!): BaseState!
        device_action(id: ID!, action: String!, args: [String]): BaseState!
    }
'''


def get_types(cls, names=[]):
    name = cls.graphql_name
    result = ''
    if name in names: return ''
    names.append(name)
    for child_cls in cls.children_model_classes.values():
        result += get_types(child_cls['class'], names)
    parent_names = [parent.__name__ for parent in cls.__mro__]
    interface = ''
    if 'DeviceStatesModel' in parent_names:
        interface = 'BaseState'
    elif 'DevicesModel' in parent_names:
        interface = 'Device'
    return result + cls.to_graphql_type(interface)


def mkschema(models_classes):
    global type_defs
    for cls in models_classes:
        type_defs += get_types(cls)
    return make_executable_schema(gql(type_defs), [query, mutation, state, device])
