import numpy as np
from core.world import World
import random


class CopterWorld(World):

    def __init__(self, config):
        self.speed_noise_level = config['speed_noise']
        self.altitude_noise_level = config['altitude_noise']
        self.sy_min = config['sy_min']
        self.sy_max = config['sy_max']
        self.last_sy = 0.0
        World.__init__(self, config)

    def setInitY(self, init_y):
        self.init_state['y'] = init_y
        self.state['y'] = init_y

    def peek(self, action):
         # set parameters of copter
        dt = self.dt
        sy = self.boundSpeedInput(action['speed_y'])  # speed input

        s = self.state

        s_noise = self.speed_noise_level * uniform_noise()
        a_noise = self.altitude_noise_level * uniform_noise()

        y, dy, ydot = s['y'], s['dy'], s['ydot']

        # integrate
        ydot = sy + s_noise
        dy = ydot * dt
        y = y + dy + a_noise

        return {
            'y': y,
            'dy': dy,
            'ydot': ydot,
        }

    def tick(self, action):
        self.state = self.peek(action)
        return self.state

    def boundSpeedInput(self, sy):
        return max(self.sy_min, min(self.sy_max, sy))


def uniform_noise():
    return (2.0 * random.random() - 1.0)
