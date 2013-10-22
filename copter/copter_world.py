import numpy as np
from core.world import World


class CopterWorld(World):

    def __init__(self, dt=0.01, state=None, params=None):
        if not params:
            params = {
                'm': 1.,
            }

        if not state:
            state = {
                'y': 0.,
                'ydot': 0.,
                'ydotdot': 0.
            }

        self.state = state
        self.dt = dt
        self.params = params

    def tick(self, force):
        # set parameters of pendulum
        g = 9.81
        dt = self.dt
        on = force['up']

        s = self.state
        p = self.params

        [y, ydot, ydotdot] = [s['y'], s['ydot'], s['ydotdot']]
        m = p['m']

        # update accelerations
        ydotdot = on * (m * g + 1) - m * g;

        # integrate
        ydot = ydot + ydotdot * dt
        y = y + ydot * dt

        # put all the variables back into the self.state
        [s['y'], s['ydot'], s['ydotdot']] = [y, ydot, ydotdot]
