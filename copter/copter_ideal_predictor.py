from core.predictor import Predictor
import copter_model_params

class CopterIdealPredictor(Predictor):

    def getModelParams(self):
        return copter_model_params.MODEL_PARAMS

    """ Public """

    def setWorld(self, world):
        self.world = world

    def learn(self, state, force): 
        state = self.world.peek(force)
        return {
            'y': state['y'],
            'dy': state['dy']
        }