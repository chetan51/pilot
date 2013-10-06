from pendulum.pendulum_controller import PendulumController

FORCE_RANGE = 40.
NUM_CANDIDATES = 40


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
        d = FORCE_RANGE / NUM_CANDIDATES
        h = FORCE_RANGE / 2
        candidates = map(lambda i: -h + d * i, range(NUM_CANDIDATES + 1))
        return sorted(candidates, key=lambda c: abs(c))
