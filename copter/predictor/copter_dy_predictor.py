from core.predictor import Predictor
import copter_model_params


class CopterDyPredictor(Predictor):

    def getModelParams(self):
        return copter_model_params.MODEL_PARAMS

    def modelInputFromStateAndAction(self, state, action):
        return {
            'dy':      state['dy'],
            'ydot':    state['ydot'],
            'ydotdot': state['ydotdot'],
            'speed_y': action['speed_y']
        }

    def stateFromPrediction(self, prediction, init_state):
        prediction_step = self.predictionSteps()[0]
        dy = prediction[prediction_step]
        y = init_state['y'] + dy

        return {
            'y': y,
            'dy': dy
        }
