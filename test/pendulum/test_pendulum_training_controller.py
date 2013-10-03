import unittest
from pendulum.pendulum_training_controller import PendulumTrainingController


class TestPendulumTrainingController(unittest.TestCase):

    def setUp(self):
        self.controller = PendulumTrainingController(None)

    def testWrapped(self):
        self.assertEqual(self.controller.wrapped(2, -10, 10), 2)
        self.assertEqual(self.controller.wrapped(10, -10, 10), 10)
        self.assertEqual(self.controller.wrapped(12, -10, 10), 8)
        self.assertEqual(self.controller.wrapped(20, -10, 10), 0)
        self.assertEqual(self.controller.wrapped(22, -10, 10), -2)
        self.assertEqual(self.controller.wrapped(30, -10, 10), -10)
        self.assertEqual(self.controller.wrapped(32, -10, 10), -8)
        self.assertEqual(self.controller.wrapped(40, -10, 10), 0)
        self.assertEqual(self.controller.wrapped(42, -10, 10), 2)
        self.assertEqual(self.controller.wrapped(42.4, -10, 10), 2.4)

        self.assertEqual(self.controller.wrapped(5, -4, 0), -3)

if __name__ == '__main__':
    unittest.main()
