from core.predictor import Predictor
import pendulum_model_params


class PendulumPredictor(Predictor):

    def getModelParams(self):
        return pendulum_model_params.MODEL_PARAMS

    def modelInputFromStateAndForce(self, state, force):
        return {
            'theta':    state['theta'],
            'thetadot': state['thetadot'],
            'force_x':  force['x']
        }

    def stateFromModelResult(self, result, init_state):
    #     predictions = result.inferences['multiStepBestPredictions']
    #     return {'theta': predictions[self.prediction_step]}
        return {'theta': self.expectation(result.inferences['multiStepPredictions'])}
