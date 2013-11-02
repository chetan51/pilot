class Runner:

    def __init__(self, config, world, predictor, controller, learning_enabled=False, target_y=0.):
        self.config = config
        self.world = world
        self.predictor = predictor
        self.controller = controller
        self.learning_enabled = learning_enabled
        self.target_y = target_y

        self.loggers = []

        self.i = 0
        self.run = 0

    """ Public """

    def tick(self):
        self.i += 1
        state = self.world.observe()

        if self.shouldBeginNewRun(state):
            self.newRun()
            return

        action = self.controller.act(state, self.predictor)

        if self.learning_enabled:
            prediction = self.predictor.learn(state, action)
        else:
            prediction = self.predictor.predict(state, action)

        self.log(state, action, prediction)

        self.world.tick(action)

    def newRun(self):
        self.reset()
        self.run += 1

        print "Beginning a new run (" + str(self.run) + ")..."

        if self.learning_enabled:
            print "Checkpointing predictor..."
            self.predictor.checkpoint()

    def setTarget(self, target):
        self.controller.setTarget(target)
        self.predictor.setTarget(target)

    def addLogger(self, logger):
        self.loggers.append(logger)

    """ Private """

    def reset(self):
        print "Resetting..."
        self.world.resetState()
        self.predictor.resetState()
        self.controller.resetState()

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
