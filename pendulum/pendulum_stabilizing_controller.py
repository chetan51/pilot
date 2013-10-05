from pendulum.pendulum_controller import PendulumController


class PendulumStabilizingController(PendulumController):

    def __init__(self, optimizer):
        PendulumController.__init__(self, optimizer)
        self.last_force = 0

    def act(self, state, predictor):
        f = self.force(self.last_force)
        self.last_force = f
        return {'x': f}

    def cost(self, state):
        return 0

    def force(self, i):
        return 0
