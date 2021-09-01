from vesla_pymvc import Model

class PluginsModel(Model):
    schema = {
        **Model.schema,
        'module_name': {
            'type': 'string',
            'required': True,
        },
        'version': { 'type': 'string' },
        'description': { 'type': 'string' },
        'config': {
            'type': 'dict',
            'default': {},
        },
    }
