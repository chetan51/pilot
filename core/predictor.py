import os
from nupic.frameworks.opf.modelfactory import ModelFactory


class Predictor:

    def __init__(self, serialization_config):
        params = self.getModelParams()
        save_path = serialization_config['path']

        if os.path.exists(os.path.abspath(save_path)):
            self.model = ModelFactory.loadFromCheckpoint(
                serialization_config['path'])
        else:
            self.model = ModelFactory.create(params)

        self.save_path = save_path
        self.save_freq = serialization_config['save_freq']
        self.num_calls = 0

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
        self.num_calls += 1
        if self.num_calls % self.save_freq == 0:
            self.model.save(os.path.abspath(self.save_path))
        result = self.model.run(self.modelInputFromStateAndForce(state, force))

        return self.stateFromModelResult(result)

    def enableLearning(self):
        self.model.enableLearning()

    def disableLearning(self):
        self.model.disableLearning()
