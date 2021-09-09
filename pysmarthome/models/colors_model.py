from durc import Model, clone


class ColorsModel(Model):
    schema = {
        **Model.schema,
        'label': { 'type': 'string', 'default': '' },
        'name': { 'type': 'string', 'default': '' },
        'rgb': { 'type': 'list', 'default': [255, 255, 255] },
    }
