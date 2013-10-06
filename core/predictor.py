import os
from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self, serialization_config):
        self.model_params = self.getModelParams()
        self.prediction_step = self.model_params['predictionSteps'][0]
        self.save_freq = serialization_config['save_freq']
        self.num_calls = 0

        self.model_path = serialization_config['path']
        self.initModel()

    """ To be overridden """

    def getModelParams(self):
        print "getModelParams needs to be overridden"

    def modelInputFromStateAndForce(self, state, force):
        return {}

    def stateFromModelResult(self, result):
        return {}

    """ Public """

    def learn(self, state, force):
        self.checkpoint()
        result = self.model.run(self.modelInputFromStateAndForce(state, force))
        return self.stateFromModelResult(result)

    def enableLearning(self):
        self.model.enableLearning()

    def disableLearning(self):
        self.model.disableLearning()

    def checkpoint(self):
        self.num_calls += 1
        if self.num_calls % self.save_freq == 0:
            self.model.save(os.path.abspath(self.model_path))

    """ Private """

    def initModel(self):
        if os.path.exists(os.path.abspath(self.model_path)):
            self.model = ModelFactory.loadFromCheckpoint(self.model_path)
        else:
            self.model = ModelFactory.create(self.model_params)

        predicted_field = self.model_params['predictedField']
        if predicted_field:
            self.model.enableInference({'predictedField': predicted_field})
