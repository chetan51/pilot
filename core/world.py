class World:

    def __init__(self, dt, state, params):
        self.state = state
        self.dt = dt
        self.params = params

    def observe(self):
        return self.state

    def tick(self, force):
        print "tick needs to be overridden"
