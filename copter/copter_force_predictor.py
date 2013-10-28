from core.predictor import Predictor
import copter_force_model_params as model_params


class CopterForcePredictor(Predictor):

    def getModelParams(self):
        return model_params.MODEL_PARAMS

    def setTarget(self, target):
        self.target = target

    def modelInputFromStateAndForce(self, state, force):
        return {
            'dtarget': state['y'] - self.target,
            'ydot':    state['ydot'],
            'force_y': force['y']
        }
