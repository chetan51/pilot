from core.predictor import Predictor
import copter_model_params


class CopterIdealPredictor(Predictor):

    def getModelParams(self):
        return copter_model_params.MODEL_PARAMS

    def modelInputFromStateAndForce(self, state, force):
        return {
            'dy':      state['dy'],
            'ydot':    state['ydot'],
            'ydotdot': state['ydotdot'],
            'force_y': force['y']
        }

    def stateFromModelResult(self, result, init_state, dt=0.01): # assumption made that time step is static
    #     predictions = result.inferences['multiStepBestPredictions']
    #     return {'dy': predictions[self.prediction_step]}
        ydot,ydotdot = init_state['ydot'], init_state['ydotdot']
        ydot = ydot + ydotdot*dt
        dy = ydot*dt
        y = init_state['y'] + dy

        return {
            'y': y,
            'dy': dy
        }
