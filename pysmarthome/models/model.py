from cerberus import Validator
from pysmarthome.utils import update_dict_fields, clone
import uuid


class Model:
    schema = {
        'id': {
            'type': 'string',
            'required': True,
            'default_setter': lambda _: str(uuid.uuid4())
        }
    }
    collection = ''
    validation_opts = {}
    children_model_classes = {}


    def __init__(self, db=None, **data):
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
        attrs = self.schema_attrs
        updated = {}
        for k, v in data.items():
            if type(v) == dict and k in attrs:
                updated_dict = attrs[k] | v
                if updated_dict != attrs[k]:
                    updated[k] = updated_dict
            elif k not in attrs or v != attrs[k]:
                updated[k] = v
        resulting_attrs = attrs | updated
        try:
            self.validate(resulting_attrs)
        except Exception as e:
            raise e
        resulting_attrs = self.normalize(resulting_attrs)
        defaults_appended = dict(filter(lambda a: a[0] not in attrs and
            a[0] not in updated, resulting_attrs.items()))
        updated |= defaults_appended
        for k, v in updated.items():
            setattr(self, k, v)
        return updated


    @classmethod
    def normalize(cls, data):
        v = Validator(cls.schema, **cls.validation_opts)
        return v.normalized(data)


    @classmethod
    def validate(cls, data):
        v = Validator(cls.schema, **cls.validation_opts)
        if not v.validate(data):
            raise Exception(v.errors)


    @property
    def attrs(self):
        return dict([(k, v) for k, v in self.__dict__.items()])


    @property
    def schema_attrs(self):
        return dict ([(k, v) for k, v in self.attrs.items() if k in self.schema])


    @classmethod
    def load_from_data(cls, db, **data):
        m = cls(db, **data)
        for k, child in cls.children_model_classes.items():
            child = child['class'].load(db, id=m.id)
            m.append_child(k, child)
        return m


    @classmethod
    def create_from_data(cls, db, **data):
        m = cls(db, **data)
        for k, child in cls.children_model_classes.items():
            attrs = child['attrs'] if 'attrs' in child else {}
            child = child['class'].create(db, id=m.id, **attrs)
            m.append_child(k, child)
        return m


    @classmethod
    def load(cls, db, id):
        try:
            data = db.get(id, cls.collection)
            return cls.load_from_data(db, **data)
        except Exception as e:
            raise e


    @classmethod
    def load_one(cls, db):
        try:
            data = db.get_one(cls.collection)
            return cls.load_from_data(db, **data)
        except Exception as e:
            raise e


    @classmethod
    def load_all(cls, db):
        try:
            data = db.get_all(cls.collection)
            models = []
            for entry in data:
                models.append(cls.load_from_data(db, **entry))
            return models
        except Exception as e:
            raise e


    @classmethod
    def create(cls, db, **data):
        try:
            m = cls.create_from_data(db, **data)
            data = m.to_dict()
            db.create(cls.collection, **data)
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


    @classmethod
    def delete(cls, db, id):
        try:
            db.delete(id, cls.collection)
            for k, model_cls in cls.children_models_classes.items():
                model_cls.delete(db, id)
            return True
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
