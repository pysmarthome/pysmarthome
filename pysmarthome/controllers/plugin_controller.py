import importlib
from . import Controller
from ..models import PluginsModel

class PluginController(Controller):
    model_class = PluginsModel

    @property
    def device_controller_classes(self): return self.module.device_controllers


    @property
    def module_name(self): return self.model.module_name


    @property
    def active(self): return self.model.active


    def __init__(self):
        self.module = None
        self.ctrl_cls = {}
        self.controllers = {}


    def toggle_active(self):
        self.model.update(active=not self.model.active)


    def init(self):
        self.module = importlib.import_module(self.module_name)
        if 'on_load' in list(self.module.__dict__.keys()):
            self.module.on_load(**self.model.config)
        for ctrl_cls in self.device_controller_classes:
            self.ctrl_cls[ctrl_cls.model_class.collection] = ctrl_cls
        children_model_classes = [(k, v.model_class) for k, v in self.ctrl_cls.items()]
        self.model.on_children_classes(children_model_classes)
        self.model.load_children()
        for col_id, models in self.model.children_models.items():
            if col_id in self.ctrl_cls:
                for m in models:
                    device_controller = self.ctrl_cls[col_id]()
                    device_controller.set_model(m)
                    self.controllers[device_controller.id] = device_controller
