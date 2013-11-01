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
        prediction = predictor.last_prediction
        f = prediction[1] if prediction else 0.
        force = self.forceDict(f)
        return force
