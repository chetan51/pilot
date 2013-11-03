class Runner:

    def __init__(self, config, world, predictor, controller, guard=None, learning_enabled=False, target_y=0., final_target_y=0.):
        self.config = config
        self.world = world
        self.predictor = predictor
        self.controller = controller
        self.guard = guard
        self.learning_enabled = learning_enabled
        self.target_y = target_y
        self.final_target_y = final_target_y

        self.setTarget(self.target_y)

        self.loggers = []

        self.i = 0
        self.run = 0
        self.disabled = False

    """ Public """

    def setTarget(self, target):
        print "Setting target to: " + str(target)
        self.controller.setTarget(target)
        self.predictor.setTarget(target)

    def tick(self):
        if self.disabled:
            return

        self.i += 1
        state = self.world.observe()

        if self.midwayThroughRun():
            self.resetPredictor()
            self.setTarget(self.final_target_y)

        if self.shouldBeginNewRun(state):
            self.checkpointPredictor()
            self.reset()

            self.setTarget(self.target_y)
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

    def checkpointPredictor(self):
        if self.learning_enabled:
            print "Checkpointing predictor... DO NOT KILL DURING THIS TIME"
            self.predictor.checkpoint()

    def runPredictor(self, state, action):
        if self.learning_enabled:
            return self.predictor.learn(state, action)
        else:
            return self.predictor.predict(state, action)

    def newRun(self):
        self.run += 1
        print "Beginning a new run (" + str(self.run) + ")..."
        self.initPredictor()

    def midwayThroughRun(self):
        iterations_per_run = self.config['iterations_per_run']

        if not self.i or self.i % iterations_per_run == 0:
            return False

        split = self.config['run_split']
        current_i = self.i % iterations_per_run

        return (current_i % int(iterations_per_run * split) == 0)

    def addLogger(self, logger):
        self.loggers.append(logger)

    """ Private """

    def initPredictor(self):
        print "Initializing predictor..."
        state = self.world.observe()
        action = self.controller.noop()
        prediction = self.runPredictor(state, action)

    def resetPredictor(self):
        print "Resetting predictor..."
        self.predictor.resetState()

    def reset(self):
        print "Resetting..."
        self.world.resetState()
        self.resetPredictor()
        self.controller.resetState()

    def log(self, state, action, prediction):
        for logger in self.loggers:
            logger.log(state, action, prediction)

    def shouldBeginNewRun(self, state):
        if self.i and (self.i % self.config['iterations_per_run'] == 0):
            return True

        return False
