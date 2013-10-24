class Controller:

    def __init__(self, optimizer):
        self.optimizer = optimizer

    def act(self, state, predictor):
        print "TODO: implement Controller.act"
        return None

    def cost(self, state):
        print "TODO: implement Controller.cost"
        return 0

    def candidates(self):
        print "TODO: implement Controller.candidates"
        return []

    def forceDict(self, f):
        print "TODO: implement Controller.forceDict"
        return {}

    """ Public """

    def resetState(self):
        return

    def bestForce(self, state, predictor):
        candidates = self.candidates()
        predictions = map(
            lambda c: predictor.learn(state, self.forceDict(c)),
            candidates
        )
        costs = map(lambda p: self.cost(p), predictions)
        min_cost = min(costs)
        i_best = costs.index(min_cost)
        return candidates[i_best]

    """ Private """

    def simulate(self, state, force):
        print "TODO: implement Controller.simulate"
        return state
