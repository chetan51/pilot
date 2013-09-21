from core.predictor import Predictor
import pendulum_model_params

class PendulumPredictor(Predictor):

    def getModelParams(self):
        return pendulum_model_params.MODEL_PARAMS