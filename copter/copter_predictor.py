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

    def stateFromPrediction(self, prediction, init_state):
        prediction_step = self.predictionSteps()[0]
        dy = prediction[prediction_step]
        y = init_state['y'] + dy

        return {
            'y': y,
            'dy': dy
        }
