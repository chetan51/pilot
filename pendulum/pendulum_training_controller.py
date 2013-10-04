from core.controller import Controller
from random import randrange
from math import sin, exp

FORCE_RANGE = 40.
B_MAX = 50000.
B_MIN = 100.
B_CENTER = 1000.
B_SPREAD = 400.


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
        return (FORCE_RANGE / 2) * sin(i / b)

    def b(self, i):
        r = B_MAX - B_MIN
        m = (-i + B_CENTER) / B_SPREAD
        return -(r / (1 + exp(m))) + B_MAX

    def heat(self, i):
        return 0
