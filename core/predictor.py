from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self):
        self.model = ModelFactory.create(self.getModelParams())

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def learn(self, state, force):
        print "TODO: implement Predictor.learn"

    def enableLearning(self):
        self.model.enableLearning()

    def disableLearning(self):
        self.model.disableLearning()
