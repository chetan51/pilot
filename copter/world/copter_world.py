import numpy as np
from core.world import World
import random


class CopterWorld(World):

    def __init__(self, config):
        self.noise_amplitude = config['noise']
        self.last_sy = 0.0
        self.sy_threshold = getSpeedChangeThreshold(config)
        World.__init__(self, config)

    def setInitY(self, init_y):
        self.init_state['y'] = init_y

    def peek(self, action):
         # set parameters of copter
        dt = self.dt
        sy = self.boundSpeedInput(action['speed_y'])  # speed input

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

    def boundSpeedInput(self, sy):
        change = sy - self.last_sy
        if change > self.sy_threshold:
            return self.last_sy + self.sy_threshold
        if change < -self.sy_threshold:
            return self.last_sy - self.sy_threshold
        return sy


def getSpeedChangeThreshold(config):
    m = config['params']['m']
    dt = config['dt']
    max_rpm, hover_rpm = config['max_rpm'], config['hover_rpm']
    return dt * ((m / hover_rpm) * max_rpm) / m
