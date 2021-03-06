from copter.controller.copter_controller import CopterController


class DronePIDController(CopterController):

    def chooseSpeed(self, state, predictor):
        y_error = self.target_y - state['y']
        s = 0.001 * y_error
        return float(s)
