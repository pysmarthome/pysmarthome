from ..utils import get_base_classes, get_methods_in


class Device:
    def __init__(self, id='', power='off'):
        self.id = id
        self.power = power


    def get_id(self):
        return self.id


    def on(self):
        # This function must return True | False
        pass


    def off(self):
        # This function must return True | False
        pass


    def toggle(self):
        # This function must return True | False
        return self.off() if self.is_on() else self.on()


    def get_power(self):
        # This function must return on | off
        return self.power


    def get_switch_power(self):
        return 'on' if self.power == 'off' else 'off'


    def set_state(self, data):
        for k, v in data.items():
            if k in self.__dict__:
                self.__dict__[k] = v


    def is_on(self):
        return self.get_power() == 'on'


    def should_update_power(self, action):
        is_on = self.is_on()
        return action == 'toggle' or \
            (action == 'off' and is_on) or \
            (action == 'on' and not is_on)


    def on_power_changed(self, new_state):
        self.power = new_state


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
