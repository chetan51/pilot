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

    def stateFromPrediction(self, prediction, init_state):
        prediction_step = self.predictionSteps()[0]

        return {
            'theta': prediction[prediction_step]
        }
