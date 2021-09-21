from durc import Model
from ..utils import rgb_to_hex


class ColorsModel(Model):
    schema = {
        **Model.schema,
        'label': { 'type': 'string', 'default': '' },
        'name': { 'type': 'string', 'default': '' },
        'rgb': { 'type': 'list', 'default': [255, 255, 255] },
    }


    def to_dict(self):
        return {
            **super().to_dict(),
            'hex': rgb_to_hex(*self.rgb),
        }
