class Controller:

    def __init__(self, optimizer):
        self.optimizer = optimizer

    """ Override """

    def act(self, state, predictor):
        print "TODO: implement Controller.act"
        return None

    def cost(self, state):
        print "TODO: implement Controller.cost"
        return 0

    def candidates(self):
        print "TODO: implement Controller.candidates"
        return []

    """ Public """

    def resetState(self):
        return
