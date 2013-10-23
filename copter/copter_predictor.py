from core.predictor import Predictor
import copter_model_params


class CopterPredictor(Predictor):

    def getModelParams(self):
        return copter_model_params.MODEL_PARAMS

    def modelInputFromStateAndForce(self, state, force):
        return {
            'dy':      state['dy'],
            'ydot':    state['ydot'],
            'ydotdot': state['ydotdot'],
            'force_y': force['y']
        }

    def stateFromModelResult(self, result):
        k_steps = self.prediction_step
        expectation = 0.0
        total_probability = 0.0
        for i in result.inferences['multiStepPredictions'][k_steps]:
            expectation += float(i) * float(
                result.inferences['multiStepPredictions'][k_steps][i])
            total_probability += float(
                result.inferences['multiStepPredictions'][k_steps][i])
        expectation = expectation / total_probability
        return {'dy': expectation}

    # previous version:
    # def stateFromModelResult(self, result):
    #     predictions = result.inferences['multiStepBestPredictions']
    #     return {'dy': predictions[self.prediction_step]}
