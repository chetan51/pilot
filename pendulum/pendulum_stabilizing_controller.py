from pendulum.pendulum_controller import PendulumController

FORCE_RANGE = 40.
NUM_CANDIDATES = 50


class PendulumStabilizingController(PendulumController):

    def act(self, state, predictor):
        return self.force_dict(self.best_force(state, predictor))

    def cost(self, state):
        return state['theta']

    def candidates(self):
        d = FORCE_RANGE / NUM_CANDIDATES
        h = FORCE_RANGE / 2
        candidates = map(lambda i: -h + d * i, range(NUM_CANDIDATES + 1))
        return sorted(candidates, key=lambda c: abs(c))
