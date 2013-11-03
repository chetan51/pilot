import numpy as np
from core.world import World

class CopterWorld(World):

    def __init__(self, dt=0.01, state=None, params=None):
        if not state:
            state = {
                'y': 0.,
                'dy': 0.,
                'ydot': 0.,
            }

        World.__init__(self, dt, state, params)

    def peek(self, action):
         # set parameters of copter
        dt = self.dt
        sy = action['speed_y']  # speed input

        s = self.state

        y, dy, ydot = s['y'], s['dy'], s['ydot']

        # integrate
        ydot = sy
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
