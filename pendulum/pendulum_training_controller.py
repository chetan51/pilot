from core.controller import Controller
from random import randrange


class PendulumTrainingController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.i = 0
        self.force_x = 0

    def act(self, state, predictor):
        if self.i and self.i % 100 == 0:
            self.force_x = randrange(-20, 20)

        self.i += 1
        return {'x': self.force_x}

    def cost(self, state):
        return 0
