from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self):
        params = self.getModelParams()
        self.model = ModelFactory.create(params)

        predicted_field = params['predictedField']
        if predicted_field:
            self.model.enableInference({'predictedField': predicted_field})
        self.prediction_step = params['predictionSteps'][0]

    """ To be overridden """

    def getModelParams(self):
        print "getModelParams needs to be overridden"

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
