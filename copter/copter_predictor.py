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

    def stateFromModelResult(self, result, init_state):
    #     predictions = result.inferences['multiStepBestPredictions']
    #     return {'dy': predictions[self.prediction_step]}
        dy = self.expectation(result.inferences['multiStepPredictions'])
        y = init_state['y'] + dy

        return {
            'y': y,
            'dy': dy
        }
