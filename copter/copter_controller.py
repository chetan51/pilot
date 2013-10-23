from core.controller import Controller


class CopterController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.i = 0

    def act(self, state, predictor):
        self.i += 1
        return self.force(0)

    def force(self, force_y):
        return {'y': force_y}
