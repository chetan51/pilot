from core.guard import Guard


class DroneGuard(Guard):

    def check(self, state, action):
        return state['y'] < 3000
