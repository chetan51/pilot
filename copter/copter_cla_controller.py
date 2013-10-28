from core.controller import Controller


class CopterCLAController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    """ Private """

    def forceDict(self, force_y):
        return {'y': force_y}

    def act(self, state, predictor):
        last_prediction = predictor.last_prediction

        if not last_prediction:
            return self.forceDict(0.)

        return self.forceDict(last_prediction[1])
