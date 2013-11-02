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

    def speedDict(self, s):
        print "TODO: implement Controller.speedDict"
        return {}

    """ Public """

    def resetState(self):
        return

    def bestSpeed(self, state, predictor):
        candidates = self.candidates()

        predictions = map(
            lambda c: predictor.predict(state, self.speedDict(c)),
            candidates
        )
        costs = map(
            lambda p: self.cost(predictor.stateFromPrediction(p, state)),
            predictions
        )

        min_cost = min(costs)
        i_best = costs.index(min_cost)

        return candidates[i_best]
