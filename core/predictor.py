import os
from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self, config):
        self.model_params = self.getModelParams()
        self.is_learning_enabled = True
        self.last_prediction = None

        self.model_path = config['serialization']['path']

        self.initModel()

    """ To be overridden """

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def modelInputFromStateAndAction(self, state, action):
        return {}

    # Optional, only for predictors whose predicted field is a state field
    def stateFromPrediction(self, prediction, init_state):
        return {}

    """ Public """

    def learn(self, state, action):
        input = self.modelInputFromStateAndAction(state, action)
        result = self.model.run(input)
        prediction = self.predictionFromModelResult(result)
        self.last_prediction = prediction
        return prediction

    def predict(self, state, action):
        input = self.modelInputFromStateAndAction(state, action)

        self.disableLearning()
        result = self.model.run(input)
        self.enableLearning()

        prediction = self.predictionFromModelResult(result)
        self.last_prediction = prediction
        return prediction

    def enableLearning(self):
        self.is_learning_enabled = True
        self.model.enableLearning()

    def disableLearning(self):
        self.is_learning_enabled = False
        self.model.disableLearning()

    def resetState(self):
        self.model.resetSequenceStates()
        self.last_prediction = None

    def checkpoint(self):
        if self.is_learning_enabled:
            self.model.save(os.path.abspath(self.model_path))

    """ Helpers """

    def predictionSteps(self):
        return self.model_params['predictionSteps']

    def predictionFromModelResult(self, result):
        prediction = result.inferences['multiStepBestPredictions']
        return prediction

    """ Private """

    def initModel(self):
        if os.path.exists(os.path.abspath(self.model_path)):
            self.model = ModelFactory.loadFromCheckpoint(
                os.path.relpath(self.model_path))
        else:
            self.model = ModelFactory.create(self.model_params)

        predicted_field = self.model_params['predictedField']
        if predicted_field:
            self.model.enableInference({'predictedField': predicted_field})
