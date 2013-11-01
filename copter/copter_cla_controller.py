from core.controller import Controller


class CopterCLAController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.target_y = 0  # default

    """ Public """

    def setTarget(self, y):
        self.target_y = y

    """ Private """

    def speedDict(self, speed_y):
        return {'y': speed_y}

    def act(self, state, predictor):
        prediction = predictor.last_prediction
        s = prediction[1] if prediction else 0.
        speed = self.speedDict(s)
        return speed
