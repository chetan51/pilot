from copter.controller.copter_controller import CopterController
from math import exp, floor
from random import random

E_MIN = 0.
E_MAX = 1.
E_CENTER = 500000.
E_SPREAD = 50000.

R_MIN = 1.
R_MAX = 2500.
R_CENTER = 10000.
R_SPREAD = 5000.


class CopterTestingController(CopterController):

    def __init__(self, optimizer, epsilon=None, inertia=None):
        CopterController.__init__(self, optimizer)
        
        self.i = 0
        self.last_speed = 0

        self.epsilon_override = epsilon
        self.inertia_override = inertia
        self.repeat_for = self.inertia(self.i)

    """ Private """

    def resetState(self):
        return  # do nothing

    def candidates(self):
        return [0., 1.]

    def cost(self, state):
        return abs(state['y'] - self.target_y)

    def act(self, state, predictor):
        self.i += 1
        self.repeat_for -= 1
        r = max(floor(self.repeat_for), 0)

        if (r):
            speed = self.last_speed
        else:
            self.repeat_for = floor(self.inertia(self.i))
            speed = self.chooseSpeed(state, predictor)

        self.last_speed = speed
        return self.actionFromSpeed(speed)

    def chooseSpeed(self, state, predictor):
        exploit = random() < self.epsilon(self.i)

        if exploit:
            # print "(Exploiting)"
            f = self.bestSpeed(state, predictor)
        else:
            # print "(Exploring)"
            f = (random() > 0.5)

        return float(f)

    def epsilon(self, i):
        if self.epsilon_override != None:
            return self.epsilon_override

        range = E_MAX - E_MIN
        m = (-i + E_CENTER) / E_SPREAD
        e = (range / (1 + exp(m)))
        return e

    def inertia(self, i):
        if self.inertia_override != None:
            return self.inertia_override

        range = R_MAX - R_MIN
        m = (-i + R_CENTER) / R_SPREAD
        r = -(range / (1 + exp(m))) + R_MAX
        return r

    """ Helpers """

    def bestSpeed(self, state, predictor):
        raise Exception("test")
        candidate_speeds = self.candidates()

        candidate_actions = [self.actionFromSpeed(c) for c in candidate_speeds]
        
        predictions = predictor.imagine(state, candidate_actions)
        
        costs = map(
            lambda p: self.cost(predictor.stateFromPrediction(p, state)),
            predictions
        )

        min_cost = min(costs)
        i_best = costs.index(min_cost)

        return candidates[i_best]