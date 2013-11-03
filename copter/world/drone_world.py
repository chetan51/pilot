import numpy as np
from core.world import World
import random
import libardrone


class DroneWorld(World):

    def __init__(self, config, drone=None):
        World.__init__(self, config)

        self.last_sy = 0.0
        self.sy_threshold = getSpeedChangeThreshold(config)
        self.sy_max = config['sy_max']
        self.last_y = 0.0

        self.drone = drone if drone else libardrone.ARDrone()

    def setInitY(self, init_y):
        self.init_state['y'] = init_y

    def peek(self, action):
         # set parameters of copter
        sy = self.boundSpeedInput(action['speed_y'])  # speed input
        sy = self.convertSpeed(sy)

        state = self.drone.navdata

        if 0 not in state:
            self.terminate()
            return

        y = state[0]['altitude']
        dy = y - self.last_y
        ydot = state[0]['vy']

        self.drone.set_speed(sy)

        return {
            'y': y,
            'dy': dy,
            'ydot': ydot,
        }

    def tick(self, action):
        self.state = self.peek(action)
        return self.state

    def boundSpeedInput(self, sy):
        change = sy - self.last_sy
        if change > self.sy_threshold:
            return min(self.last_sy + self.sy_threshold, self.sy_max)
        if change < -self.sy_threshold:
            return max(- self.sy_max, self.last_sy - self.sy_threshold)
        return sy

    def terminate(self):
        World.terminate(self)
        return self.drone.land()

    def convertSpeed(self, speed):
        return speed / self.sy_max


def getSpeedChangeThreshold(config):
    m = config['params']['m']
    dt = config['dt']
    max_rpm, hover_rpm = config['max_rpm'], config['hover_rpm']
    g = 9.81
    return dt * ((m * g / hover_rpm) * max_rpm) / m
