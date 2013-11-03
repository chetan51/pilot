from core.guard import Guard


class CopterGuard(Guard):

    def check(self, state, action):
        return True
