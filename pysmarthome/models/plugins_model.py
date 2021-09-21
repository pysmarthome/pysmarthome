from durc import Model

class PluginsModel(Model):
    schema = {
        **Model.schema,
        'module_name': {
            'type': 'string',
            'required': True,
        },
        'active': { 'type': 'boolean',  'default': True, 'required': True },
        'version': { 'type': 'string' },
        'description': { 'type': 'string' },
        'config': {
            'type': 'dict',
            'default': {},
        },
    }
