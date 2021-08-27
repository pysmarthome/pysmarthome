from .model import Model, clone

class ManagerConfigsModel(Model):
    schema = clone(Model.schema)
