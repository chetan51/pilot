from core.controller import Controller


class PendulumTrainingController(Controller):

    def act(self, state, predictor):
        return {'x': 0}

    def cost(self, state):
        return 0
