from abc import ABC, abstractmethod
from ..utils import get_base_classes, get_methods_in
from pysmarthome.models import DeviceModel


class Device(ABC):
    model_class = DeviceModel
    controller_api = ''


    def __init__(self):
        self.model = self.model_class()
        self._dev = None
        self._controller = None


    @property
    def id(self): return self.model.id


    @property
    def name(self): return self.model.name


    @property
    def mac_addr(self): return self.model.mac_addr


    @abstractmethod
    def on(self):
        # This function must return True | False
        pass


    @abstractmethod
    def off(self):
        # This function must return True | False
        pass


    def toggle(self):
        # This function must return True | False
        return self.off() if self.is_on() else self.on()


    def get_power(self):
        # This function must return on | off
        return self.model.state.power


    def get_switch_power(self):
        return 'on' if self.model.state.power == 'off' else 'off'


    @property
    def dev(self): return self._dev


    @dev.setter
    def dev(self, d): self._dev = d


    @property
    def controller(self): return self._controller


    @controller.setter
    def controller(self, ctrl): self._controller = ctrl


    def sync_state(self):
        # will execute getters of highest hierarchy class if they exist.
        # Its important to notice that the controllers must implement the getters
        # with the 'get_' prefix
        actions = self.get_actions()
        state = {}
        for k in self.model.state.schema['state']['schema'].keys():
            getter_id = f'get_{k}'
            if getter_id in actions:
                state[k] = actions[getter_id](self)
        self.set_state(**state)




    def update(self, **data):
        try:
            self.model.update(**data)
        except Exception as e:
            raise e


    def set_state(self, **data):
        try:
            self.model.state.update(state=data)
        except Exception as e:
            print(f'syncing failed: {e}')


    def is_on(self):
        return self.get_power() == 'on'


    def should_update_power(self, action):
        is_on = self.is_on()
        return action == 'toggle' or \
            (action == 'off' and is_on) or \
            (action == 'on' and not is_on)


    def on_power_changed(self, new_state):
        self.set_state(power=new_state)


    def get_actions(self):
        bases = get_base_classes(self.__class__)
        methods = get_methods_in(*bases)
        actions = {}
        for k, f in methods:
            if k not in actions:
                actions[k] = f
        return actions


    def trigger_action(self, action_id, **params):
        try:
            actions = self.get_actions()
            if action_id in ['on', 'off', 'toggle']:
                if self.should_update_power(action_id):
                    new_state = self.get_switch_power()
                    if actions[action_id](self):
                        self.on_power_changed(new_state)
                    return True
                else:
                    return False
            if action_id in actions:
                actions[action_id](self, **params)
            return True
        except:
            return False
