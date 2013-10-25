from core.controller import Controller
from math import exp, floor
from random import random

E_MIN = 0.
E_MAX = 1.
E_CENTER = 50.
E_SPREAD = 50.

R_MIN = 1.
R_MAX = 100.
R_CENTER = 1000.
R_SPREAD = 700.


class CopterController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default
        self.i = 0
        self.last_force = 0
        self.repeat_for = self.responsivity(self.i)

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    """ Private """

    def resetState(self):
        return  # do nothing

    def candidates(self):
        return [0., 1.]

    def cost(self, state):
        return abs(state['y'] - self.target_y)

    def forceDict(self, force_y):
        return {'y': force_y}

    def act(self, state, predictor):
        self.i += 1
        self.repeat_for -= 1
        r = floor(self.repeat_for)

        if (r):
            force = self.last_force
        else:
            self.repeat_for = floor(self.responsivity(self.i))
            force = self.chooseForce(state, predictor)

        self.last_force = force
        return self.forceDict(force)

    def chooseForce(self, state, predictor):
        exploit = random() < self.epsilon(self.i)

        if exploit:
            f = self.bestForce(state, predictor)
        else:
            f = (random() > 0.5)

        return float(f)

    def epsilon(self, i):
        range = E_MAX - E_MIN
        m = (-i + E_CENTER) / E_SPREAD
        e = (range / (1 + exp(m)))
        return e

    def responsivity(self, i):
        range = R_MAX - R_MIN
        m = (-i + R_CENTER) / R_SPREAD
        r = -(range / (1 + exp(m))) + R_MAX
        return r
