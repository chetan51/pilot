from core.controller import Controller


class PendulumController(Controller):

    def __init__(self, optimizer):
        Controller.__init__(self, optimizer)
        self.i = 0

    def forceDict(self, force_x):
        return {'x': force_x}
