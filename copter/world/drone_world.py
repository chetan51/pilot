import numpy as np
from core.world import World
import random
import libardrone


class DroneWorld(World):

    def __init__(self, config, drone=None):
        self.last_sy = 0.0
        self.sy_threshold = getSpeedChangeThreshold(config)
        self.sy_max = config['sy_max']
        self.drone = drone if drone else libardrone.ARDrone()
        self.last_y = 0.0
        World.__init__(self, config)

    def setInitY(self, init_y):
        self.init_state['y'] = init_y

    def peek(self, action):
         # set parameters of copter
        sy = self.boundSpeedInput(action['speed_y'])  # speed input
        sy = convertSpeed(sy)

        drone.set_speed(sy)
        state = drone.navdata

        if 0 not in state:
            self.terminate()
            return

        y = state[0]['altitude']
        dy = y - self.last_y
        ydot = state[0]['vy']

        return {
            'y': y,
            'dy': dy,
            'ydot': ydot,
        }

    def tick(self, action):
        p = self.peek(action)
        s = self.state

        s['y'], s['dy'], s['ydot'] = p['y'], p['dy'], p['ydot']

        return s

    def boundSpeedInput(self, sy):
        change = sy - self.last_sy
        if change > self.sy_threshold:
            return min(self.last_sy + self.sy_threshold, self.sy_max)
        if change < -self.sy_threshold:
            return max(- self.sy_max, self.last_sy - self.sy_threshold)
        return sy

    def terminate():
        return self.drone.land()


def getSpeedChangeThreshold(config):
    m = config['params']['m']
    dt = config['dt']
    max_rpm, hover_rpm = config['max_rpm'], config['hover_rpm']
    g = 9.81
    return dt * ((m * g / hover_rpm) * max_rpm) / m


def convertSpeed(speed):
    return speed / self.sy_max


def uniform_noise():
    return (2.0 * random.random() - 1.0)
