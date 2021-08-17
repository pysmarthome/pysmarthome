from .model import Model


class PcActions(Model):
    schema = Model.schema | {
        'actions': {
            'type': 'dict',
            'allow_unknown': {
                'type': 'dict',
                'schema': {
                    'name': { 'type': 'string' },
                    'path': { 'type': 'string' },
                    'data': { 'type': 'string' },
                },
            },
        },
    }
    collection = 'pc_actions'


    def get(self, id):
        if id in self.actions:
            return self.actions[id]
        return None
