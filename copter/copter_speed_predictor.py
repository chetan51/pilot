from core.predictor import Predictor
import copter_speed_model_params as model_params


class CopterSpeedPredictor(Predictor):

    def getModelParams(self):
        return model_params.MODEL_PARAMS

    def setTarget(self, target):
        self.target = target

    def modelInputFromStateAndForce(self, state, speed):
        dtarget = state['y'] - self.target
        return {
            'dtarget': dtarget,
            'ydot':    state['ydot'],
            'speed_y': speed['y']
        }
