from pendulum.pendulum_controller import PendulumController
from random import randrange
from math import sin, exp, floor

FORCE_RANGE = 40.
B_MAX = 50000.
B_MIN = 100.
B_CENTER = 2000.
B_SPREAD = 10000.
R_MIN = 0.
R_MAX = 10.
R_CENTER = 100000.
R_SPREAD = 1000.


class PendulumTrainingController(PendulumController):

    def act(self, state, predictor):
        self.i += 1
        return {'x': self.force(self.i)}

    def cost(self, state):
        return 0

    def force(self, i):
        h = (FORCE_RANGE / 2)
        b = self.b(i)
        f = h * sin(i / b)
        r = int(floor(self.r(i) * 1000))
        n = randrange(-r, r) / 1000. if r else 0
        f = f + n
        f = max(min(f, h), -h)
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
