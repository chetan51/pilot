class Runner:

    def __init__(self, config, world, predictor, controller, guard=None, learning_enabled=False, target_y=0.):
        self.config = config
        self.world = world
        self.predictor = predictor
        self.controller = controller
        self.guard = guard
        self.learning_enabled = learning_enabled
        self.target_y = target_y

        self.loggers = []

        self.i = 0
        self.run = 0
        self.disabled = False

    """ Public """

    def setTarget(self, target):
        self.controller.setTarget(target)
        self.predictor.setTarget(target)

    def tick(self):
        if self.disabled:
            return

        self.i += 1
        state = self.world.observe()

        if self.shouldBeginNewRun(state):
            self.reset()
            self.newRun()
            return

        action = self.controller.act(state, self.predictor)

        if not self.sanityCheck(state, action):
            self.world.terminate()
            self.disabled = True
            return

        prediction = self.runPredictor(state, action)

        self.world.tick(action)

        self.log(state, action, prediction)

    def sanityCheck(self, state, action):
        if not self.guard:
            return True

        return self.guard.check(state, action)

    def runPredictor(self, state, action):
        if self.learning_enabled:
            return self.predictor.learn(state, action)
        else:
            return self.predictor.predict(state, action)

    def newRun(self):
        self.run += 1

        print "Beginning a new run (" + str(self.run) + ")..."

        if self.learning_enabled:
            print "Checkpointing predictor... DO NOT KILL DURING THIS TIME"
            self.predictor.checkpoint()

    def addLogger(self, logger):
        self.loggers.append(logger)

    """ Private """

    def initPredictor(self):
        print "Initializing predictor..."
        state = self.world.observe()
        action = self.controller.noop()
        prediction = self.runPredictor(state, action)

    def reset(self):
        print "Resetting..."
        self.world.resetState()
        self.predictor.resetState()
        self.controller.resetState()
        self.initPredictor()

    def log(self, state, action, prediction):
        for logger in self.loggers:
            logger.log(state, action, prediction)

    def shouldBeginNewRun(self, state):
        if self.i and (self.i % self.config['iterations_per_run'] == 0):
            return True

        if (state['y'] > self.config['y_max']) or (state['y'] < self.config['y_min']):
            return True

        if abs(state['y'] - self.target_y) < self.config['target_threshold']:
            return True

        return False
