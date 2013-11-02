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
        return self.speedDict(speed)

    # To be overridden
    def chooseSpeed(self, state, predictor):
        return 0.

    """ Helpers """

    def speedDict(self, speed_y):
        return {'y': speed_y}
