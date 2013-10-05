from core.predictor import Predictor
import pendulum_model_params


class PendulumPredictor(Predictor):

    def getModelParams(self):
        return pendulum_model_params.MODEL_PARAMS

    def modelInputFromStateAndForce(self, state, force):
        return {
            'theta':   state['theta'],
            'x':       state['x'],
            'force_x': force['x']
        }

    def stateFromModelResult(self, result):
        predictions = result.inferences['multiStepBestPredictions']
        return {'theta': predictions[self.prediction_step]}
