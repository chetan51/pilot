import numpy as np
from core.world import World
import random

class CopterWorld(World):

    def __init__(self, config):
        self.noise_amplitude = config['noise']
        World.__init__(self, config)

    def peek(self, action):
         # set parameters of copter
        dt = self.dt
        sy = action['speed_y']  # speed input

        s = self.state

        y, dy, ydot = s['y'], s['dy'], s['ydot']
        noise = self.noise_amplitude * (2.0 * random.random() - 1.0)

        # integrate
        ydot = sy + noise
        dy = ydot * dt
        y = y + dy

        return {
            'y': y,
            'dy': dy,
            'ydot': ydot,
        }

    def tick(self, action):
        s = self.peek(action)
        y, dy, ydot = s['y'], s['dy'], s['ydot']

        s = self.state

        # put all the variables back into the self.state
        s['y'], s['dy'], s['ydot'] = y, dy, ydot
        return s
