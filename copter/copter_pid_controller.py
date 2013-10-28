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

    def resetState(self):
        return  # do nothing

    def candidates(self):
        return [0., 1.]

    def cost(self, state):
        return abs(state['y'] - self.target_y)

    def forceDict(self, force_y):
        return {'y': force_y}

    def act(self, state, predictor):
        force = self.chooseForce(state, predictor)
        return self.forceDict(force)

    def chooseForce(self, state, predictor):
        y_error = self.target_y - state['y']
        ydot_error = state['ydot']
        ydotdot_error = state['ydotdot']
        f = -(-0.6 * y_error - 0.3 * ydot_error - 0.1 * ydotdot_error)/(y_error + ydot_error + ydotdot_error + 1)
        # print 'y_error: ', y_error, ' ydot_error: ', ydot_error, ' ydotdot_error: ', ydotdot_error
        # print f
        f = 0 if f < 0.5 else 1
        return float(f)

