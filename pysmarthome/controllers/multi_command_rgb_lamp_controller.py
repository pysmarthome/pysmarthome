from .rgb_lamp_controller import RgbLampController
from .multi_command_device_controller import MultiCommandDeviceController
from ..models import MultiCommandRgbLampsModel, CommandsModel
from ..models import ColorsModel
from ..utils import rgb_to_hex, hex_to_rgb, color_dist
from math import inf


class MultiCommandRgbLampController(MultiCommandDeviceController, RgbLampController):
    model_class = MultiCommandRgbLampsModel


    def on(self):
        self.send_command('on')
        return True


    def off(self):
        self.send_command('off')
        return True


    def set_brightness_by(self, n):
        self.set_int_state_attr_by('brightness', n)


    def set_brightness(self, target):
        self.set_int_state_attr_to('brightness', target)


    def set_color(self, target_color):
        db = self.model.db
        color_models = []
        for c in self.model.color_commands:
            color_models.append({
                'ctrl': ColorsModel.load(db, c.color_id),
                'cmd_id': c.command_id,
            })
        if len(color_models) == 0: return False
        if type(target_color) == str: target_color = hex_to_rgb(target_color)
        cmd_id = color_models[0]['cmd_id']
        closest_color = [255, 255, 255]
        dist = inf
        for c in color_models:
            ctrl_color = c['ctrl'].rgb
            d = min(color_dist(target_color, ctrl_color), dist)
            if d < dist:
                cmd_id = c['cmd_id']
                dist = d
                closest_color = ctrl_color
        self.send_command(cmd_id)
        self.set_state(color=rgb_to_hex(*closest_color))
        return True
