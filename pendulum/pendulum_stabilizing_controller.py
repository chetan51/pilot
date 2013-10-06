from pendulum.pendulum_controller import PendulumController

FORCE_RANGE = 40.
NUM_CANDIDATES = 10


class PendulumStabilizingController(PendulumController):

    def act(self, state, predictor):
        candidates = self.candidates()
        predictions = map(
            lambda c: predictor.learn(state, self.force(c)),
            candidates
        )
        costs = map(lambda p: self.cost(p), predictions)
        min_cost = min(costs)
        i_best = costs.index(min_cost)
        return self.force(candidates[i_best])

    def cost(self, state):
        return state['theta']

    def candidates(self):
        candidates = []
        d = FORCE_RANGE / NUM_CANDIDATES
        h = FORCE_RANGE / 2
        return map(lambda i: -h + d * i, range(NUM_CANDIDATES + 1))
