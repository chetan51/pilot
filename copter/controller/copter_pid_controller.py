from copter.controller.copter_controller import CopterController


class CopterPIDController(CopterController):

    def chooseSpeed(self, state, predictor):
        y_error = self.target_y - state['y']
        ydot_error = state['ydot']
        s = 1 * y_error - 0.6 * ydot_error
        return float(s)
