from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self):
        self.model = ModelFactory.create(self.getModelParams())

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def learn(self, state, force):
        print "TODO: implement Predictor.learn"

    def enableLearning(self):
        print "TODO: implement Predictor.enableLearning"

    def disableLearning(self):
        print "TODO: implement Predictor.disableLearning"
