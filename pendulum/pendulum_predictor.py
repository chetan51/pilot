from core.predictor import Predictor
import pendulum_model_params


class PendulumPredictor(Predictor):

    def getModelParams(self):
        return pendulum_model_params.MODEL_PARAMS

    def modelInputFromStateAndForce(self, state, force):
        return {
            'theta':   state['theta'],
            'thetadot':   state['thetadot'],
            'force_x': force['x']
        }

    def stateFromModelResult(self, result):
        k_steps = self.prediction_step
        expectation = 0.0
        total_probability = 0.0
        for i in result.inferences['multiStepPredictions'][k_steps]:
            expectation += float(i)*float(result.inferences['multiStepPredictions'][k_steps][i])
            total_probability += float(result.inferences['multiStepPredictions'][k_steps][i])
        expectation = expectation / total_probability
        return {'theta': expectation}

    # previous version:
    # def stateFromModelResult(self, result):
    #     predictions = result.inferences['multiStepBestPredictions']
    #     return {'theta': predictions[self.prediction_step]}
