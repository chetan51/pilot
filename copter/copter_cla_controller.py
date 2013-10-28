from core.controller import Controller


class CopterCLAController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default
        self.last_force = self.forceDict(0.)

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    """ Private """

    def forceDict(self, force_y):
        return {'y': force_y}

    def act(self, state, predictor):
        prediction = predictor.predict(state, self.last_force)
        force = self.forceDict(prediction[1])
        self.last_force = force
        return force
