from copter.controller.copter_controller import CopterController


class CopterPIDController(CopterController):

    def chooseSpeed(self, state, predictor):
        y_error = self.target_y - state['y']
        s = 1 * y_error
        return float(s)
