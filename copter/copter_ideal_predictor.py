from core.predictor import Predictor
import copter_model_params


class CopterIdealPredictor(Predictor):

    def __init__(self, serialization_config, world=None):
        Predictor.__init__(self, serialization_config)
        self.world = world

    def getModelParams(self):
        return copter_model_params.MODEL_PARAMS

    """ Public """

    def learn(self, state, force):
        state = self.world.peek(force)
        return {
            'y': state['y'],
            'dy': state['dy']
        }
