from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self):
        self.model = ModelFactory.create(self.getModelParams())

        predicted_field = self.getModelPredictedField()
        if predicted_field:
            self.model.enableInference({'predictedField': predicted_field})

    """ To be overridden """

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def getModelPredictedField(self):
        return None

    def modelInputFromStateAndForce(self, state, force):
        return {}

    def stateFromModelResult(self, result):
        return {}

    """ Public """

    def learn(self, state, force):
        result = self.model.run(self.modelInputFromStateAndForce(state, force))
        return self.stateFromModelResult(result)

    def enableLearning(self):
        self.model.enableLearning()

    def disableLearning(self):
        self.model.disableLearning()
