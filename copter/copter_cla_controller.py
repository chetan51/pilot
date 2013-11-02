from copter.copter_controller import CopterController


class CopterCLAController(CopterController):

    def chooseSpeed(self, state, predictor):
        prediction = predictor.last_prediction
        return prediction[1] if prediction else 0.
