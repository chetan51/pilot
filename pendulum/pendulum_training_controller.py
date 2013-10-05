from core.controller import Controller
from random import randrange
from math import sin, exp, floor

FORCE_RANGE = 40.
B_MAX = 50000.
B_MIN = 100.
B_CENTER = 2000.
B_SPREAD = 4000.
R_MIN = 0.
R_MAX = 10.
R_CENTER = 20000.
R_SPREAD = 1000.


class PendulumTrainingController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.i = 0

    def act(self, state, predictor):
        self.i += 1
        return {'x': self.force(self.i)}

    def cost(self, state):
        return 0

    def force(self, i):
        b = self.b(i)
        f = (FORCE_RANGE / 2) * sin(i / b)
        r = int(floor(self.r(i) * 1000))
        n = randrange(-r, r) / 1000. if r else 0
        f = f + n
        return f

    def b(self, i):
        range = B_MAX - B_MIN
        m = (-i + B_CENTER) / B_SPREAD
        return -(range / (1 + exp(m))) + B_MAX

    def r(self, i):
        range = R_MAX - R_MIN
        m = (-i + R_CENTER) / R_SPREAD
        r = (range / (1 + exp(m)))
        return r

    def heat(self, i):
        return 0
