from core.controller import Controller
from math import exp, floor
from random import random


class CopterPIDController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    """ Private """

    def forceDict(self, force_y):
        return {'y': force_y}

    def act(self, state, predictor):
        force = self.chooseForce(state, predictor)
        return self.forceDict(force)

    def chooseForce(self, state, predictor):
        y_error = self.target_y - state['y']
        ydot_error = state['ydot']
        f = 1 * y_error - 0.6 * ydot_error
        return float(f)
