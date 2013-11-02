import os
from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self, serialization_config):
        self.model_params = self.getModelParams()
        self.save_freq = serialization_config['save_freq']
        self.num_calls = 0
        self.is_learning_enabled = True
        self.last_prediction = None

        self.model_path = serialization_config['path']
        self.initModel()

    """ To be overridden """

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def modelInputFromStateAndForce(self, state, force):
        return {}

    # Optional, only for predictors whose predicted field is a state field
    def stateFromPrediction(self, prediction, init_state):
        return {}

    """ Public """

    def learn(self, state, force):
        self.checkpoint()
        input = self.modelInputFromStateAndForce(state, force)
        result = self.model.run(input)
        prediction = self.predictionFromModelResult(result)
        self.last_prediction = prediction
        return prediction

    def predict(self, state, force):
        input = self.modelInputFromStateAndForce(state, force)

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

    def checkpoint(self):
        if self.is_learning_enabled:
            self.num_calls += 1
            if self.num_calls % self.save_freq == 0:
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
