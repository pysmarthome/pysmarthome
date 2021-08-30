import importlib
from . import Controller
from ..models import PluginsModel

class PluginController(Controller):
    model_class = PluginsModel

    @property
    def device_controllers(self): return self.module.device_controllers

    def __init__(self):
        self.module = None


    def on_load(self, module_name='', **data):
        self.module = importlib.import_module(module_name)
        if 'on_load' in list(self.module.__dict__.keys()):
            self.module.on_load(**data['config'])


    def install(self):
        pass
