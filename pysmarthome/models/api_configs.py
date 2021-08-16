from .model import Model

class ApiConfigModel(Model):
    schema = {
        **Model.schema,
        'name': {
            'type':  'string',
            'required': True
        },
    }
    collection = 'api_configs'
    validation_opts = { 'allow_unknown': { 'type': 'string' } }
