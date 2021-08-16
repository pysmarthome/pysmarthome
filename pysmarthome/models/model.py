from cerberus import Validator
from pysmarthome.utils import update_dict_fields


class Model:
    schema = {
        'id': {
            'type': 'string',
            'required': True,
        }
    }
    collection = ''
    validation_opts = {}
    children_model_classes = {}


    def __init__(self, db=None, id='', **data):
        self.id = id
        self.db = db
        self.children_models = {}
        self.set_attrs(**data)


    def __getattr__(self, k):
        try:
            attrs = self.attrs
            if k in attrs:
                return attrs[k]

            for i, d in attrs.items():
                if type(d) == dict and k in d:
                    return d[k]
            raise KeyError
        except KeyError:
            print(f'{k} was not found in {self.id}')


    def set_attrs(self, **data):
        if not data: return {}
        attrs = self.schema_attrs
        try:
            self.validate(attrs | data)
        except Exception as e:
            raise e
        updated = {}
        for k, v in data.items():
            if k not in attrs or v != attrs[k]:
                updated[k] = v
                setattr(self, k, v)
        return updated


    def validate(self, data):
        v = Validator(self.schema, **self.validation_opts)
        if not v.validate(data):
            raise Exception(v.errors)


    @property
    def attrs(self):
        return dict([(k, v) for k, v in self.__dict__.items()])


    @property
    def schema_attrs(self):
        return dict ([(k, v) for k, v in self.attrs.items() if k in self.schema])


    @classmethod
    def load(cls, db, id):
        try:
            data = db.get(id, cls.collection)
            m = cls(db, **data)
            for k, model_cls in cls.children_model_classes.items():
                child = model_cls.load(db, id)
                m.append_child(k, child)
            return m
        except Exception as e:
            raise e


    def update(self, **data):
        try:
            updated = self.set_attrs(**data)
            if updated:
                self.db.update(self.id, self.collection, **updated)
        except Exception as e:
            raise e


    def append_child(self, id, model):
        if id not in self.children_model_classes:
            raise Exception('not in children models')
        self.children_models[id] = model
        setattr(self, id, model)


    def to_dict(self, **fields_mapping):
        try:
            attrs = self.schema_attrs
            updated_fields = update_dict_fields(attrs, **fields_mapping)
            self.validate(updated_fields)
            for child in self.children_models.values():
                updated_fields |= child.to_dict(**fields_mapping)
            return updated_fields
        except Exception as e:
            print(e)
