import numpy as np
from core.world import World
import random


class DroneWorld(World):

    def __init__(self, config, drone=None):
        World.__init__(self, config)

        self.last_sy = 0.0
        self.sy_min = config['sy_min']
        self.sy_max = config['sy_max']
        self.last_y = 0.0

        self.drone = drone

    def setup(self):
        self.drone.takeoff()

    def setInitY(self, init_y):
        self.init_state['y'] = init_y

    def observe(self):
        y = self.drone.altitude()
        ydot = self.drone.speed()
        dy = y - self.last_y

        return {
            'y': y,
            'dy': dy,
            'ydot': ydot,
        }

    def tick(self, action):
        sy = self.boundSpeedInput(action['speed_y'])  # speed input
        self.drone.setSpeed(sy)

    def resetState(self):
        World.resetState(self)
        self.drone.land()
        self.setup()

    def boundSpeedInput(self, sy):
        return max(self.sy_min, min(self.sy_max, sy))

    def terminate(self):
        World.terminate(self)
        return self.drone.land()
