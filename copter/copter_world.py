import numpy as np
from core.world import World

FY_BASE = 2.5


class CopterWorld(World):

    def __init__(self, dt=0.01, state=None, params=None):
        if not params:
            params = {
                'm': 1.,
            }

        if not state:
            state = {
                'y': 0.,
                'dy': 0.,
                'ydot': 0.,
                'ydotdot': 0.
            }

        World.__init__(self, dt, state, params)

    def tick(self, force):
        # set parameters of copter
        g = 9.81
        dt = self.dt
        fy = force['y']

        s = self.state
        p = self.params

        [y, dy, ydot, ydotdot] = [s['y'], s['dy'], s['ydot'], s['ydotdot']]
        m = p['m']

        # update accelerations
        ydotdot = (fy * FY_BASE * m * g) - (m * g)

        # integrate
        ydot = ydot + ydotdot * dt
        dy = ydot * dt
        y = y + dy

        # put all the variables back into the self.state
        [s['y'], s['dy'], s['ydot'], s['ydotdot']] = [y, dy, ydot, ydotdot]
