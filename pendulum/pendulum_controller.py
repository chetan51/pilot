from core.controller import Controller
from pendulum.pendulum_training_controller import PendulumTrainingController


class PendulumController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.trainer = PendulumTrainingController(optimizer)

    def act(self, state, predictor):
        return self.trainer.act(state, predictor)

    def cost(self, state):
        return self.trainer.cost(state)
