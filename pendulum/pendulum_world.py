import numpy as np
from core.world import World


class PendulumWorld(World):

    def __init__(self, dt=0.01, state=None, params=None, rollover=True):
        if not params:
            params = {
                'm': 1.,
                'k': 2.,
                'l': 1.
            }

        if not state:
            state = {
                'x': 0.,
                'xdot': 0.,
                'xdotdot': 0.,
                'theta_int': 0.,
                'theta': 0.,
                'thetadot': 0.,
                'thetadotdot': 0.
            }

        self.state = state
        self.dt = dt
        self.params = params
        self.rollover = rollover

    def tick(self, force):
        # set parameters of pendulum
        g = 9.81
        dt = self.dt
        fx = force['x']

        s = self.state
        p = self.params

        [x, xdot, xdotdot, theta_int, theta, thetadot, thetadotdot] = [s['x'], s['xdot'],
                                                                       s['xdotdot'], s['theta_int'], s['theta'], s['thetadot'], s['thetadotdot']]
        [m, k, l] = [p['m'], p['k'], p['l']]

        # update accelerations
        xdotdot = (np.sin(theta) / (k + 1 - np.cos(theta) ** 2)) * \
            (g * np.cos(theta) - l * thetadot ** 2) - fx / m
        thetadotdot = (xdotdot * np.cos(theta) + g * np.sin(theta)) / l

        # integrate
        thetadot = thetadot + thetadotdot * dt
        theta = theta + thetadot * dt

        if self.rollover:
            theta = theta % (2 * np.pi)

        theta_int = theta_int + theta * dt
        xdot = xdot + xdotdot * dt
        x = x + xdot * dt

        # put all the variables back into the self.state
        [s['x'], s['xdot'], s['xdotdot'], s['theta_int'], s['theta'], s['thetadot'],
            s['thetadotdot']] = [x, xdot, xdotdot, theta_int, theta, thetadot, thetadotdot]
