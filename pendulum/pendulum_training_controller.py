from core.controller import Controller
from random import randrange

FORCE_MIN = -10
FORCE_MAX = 10
DURATION_NO_FORCE = 300


class PendulumTrainingController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.i = 0
        self.raw_force_x = 0
        self.force_x = 0
        self.increasing = True

    def act(self, state, predictor):
        self.raw_force_x = self.raw_force_x + self.dx(self.i)
        self.force_x = self.wrapped(self.raw_force_x, FORCE_MIN, FORCE_MAX)

        self.i += 1
        return {'x': self.force_x}

    def cost(self, state):
        return 0

    def dx(self, i):
        return 0.05 if i > DURATION_NO_FORCE else 0

    def heat(self, i):
        return 0

    def wrapped(self, x, min, max):
        mid = (min + max) / 2.
        range = max - min
        norm_x = x % (range * 2)

        if norm_x > max and norm_x < max + range:
            return max + (max - mid) - norm_x
        elif norm_x >= max + range:
            return norm_x - (range * 2)

        return round(norm_x, 4)
