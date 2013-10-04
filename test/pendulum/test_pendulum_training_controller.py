import unittest
from pendulum.pendulum_training_controller import PendulumTrainingController


class TestPendulumTrainingController(unittest.TestCase):

    def setUp(self):
        self.controller = PendulumTrainingController(None)

if __name__ == '__main__':
    unittest.main()
