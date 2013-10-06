from pendulum.pendulum_controller import PendulumController

FORCE_RANGE = 40.
NUM_CANDIDATES = 100


class PendulumStabilizingController(PendulumController):

    def act(self, state, predictor):
        candidates = self.candidates()
        predictions = map(
            lambda c: predictor.learn(state, self.force(c)),
            candidates
        )
        thetas = map(lambda p: p['theta'], predictions)
        index = thetas.index(max(thetas))
        return self.force(candidates[index])

    def cost(self, state):
        return 0

    def candidates(self):
        candidates = []
        d = FORCE_RANGE / NUM_CANDIDATES
        h = FORCE_RANGE / 2
        return map(lambda i: -h + d * i, range(NUM_CANDIDATES + 1))
