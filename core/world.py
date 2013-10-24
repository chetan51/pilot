from copy import deepcopy


class World:

    def __init__(self, dt, state, params):
        self.state = state
        self.init_state = deepcopy(state)

        self.dt = dt
        self.init_dt = dt

        self.params = params

    def observe(self):
        return self.state

    def tick(self, force):
        print "tick needs to be overridden"

    def resetState(self):
        self.state = deepcopy(self.init_state)
        self.dt = self.init_dt
