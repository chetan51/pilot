class Controller:

    def __init__(self, optimizer):
        self.optimizer = optimizer

    def act(self, state, predictor):
        print "TODO: implement Controller.act"
        return None

    def cost(self, state):
        return 0

    """Private"""

    def simulate(self, state, force):
        print "TODO: implement Controller.simulate"
        return state
