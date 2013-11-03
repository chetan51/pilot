from core.controller import Controller


class CopterController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    def act(self, state, predictor):
        speed = self.chooseSpeed(state, predictor)
        return self.actionFromSpeed(speed)

    # To be overridden
    def chooseSpeed(self, state, predictor):
        return 0.

    """ Private """

    def noop(self):
        return self.actionFromSpeed(0.)

    """ Helpers """

    def actionFromSpeed(self, s):
        return {'speed_y': s}
