from copy import deepcopy


class World:

    def __init__(self, config):
        self.state = config['state']
        self.init_state = deepcopy(self.state)

        self.dt = config['dt']
        self.init_dt = self.dt

        self.params = config['params']

    def observe(self):
        return self.state

    def tick(self, force):
        print "tick needs to be overridden"

    def resetState(self):
        self.state = deepcopy(self.init_state)
        self.dt = self.init_dt

    def terminate(self):
        pass
