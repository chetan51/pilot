#!/usr/bin/env python

import sys
import numpy as np
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_controller import PendulumController
from pendulum.pendulum_predictor import PendulumPredictor


def run(theta):
    world = PendulumWorld()
    controller = PendulumController(None)
    predictor = PendulumPredictor()

    world.state['theta'] = np.deg2rad(theta)

    while True:
        state = world.observe()

        predictor.disableLearning()
        force = controller.act(state, predictor)

        predictor.enableLearning()
        predicted_state = predictor.learn(state, force)

        printTimestep(state, force, predicted_state)
        world.tick(force)


def printTimestep(state, force, predicted_state):
    print "[observed]  angle: " + to_str(np.rad2deg(state['theta'])) + "\t" + "position: " + to_str(state['x']) + "\t" + "force: " + to_str(force['x'])
    print "[predicted] angle: " + to_str(np.rad2deg(predicted_state['theta'])) + "\t" + "position: " + to_str(predicted_state['x'])


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    if len(sys.argv) > 1:
        theta = int(sys.argv[1])
        run(theta)
    else:
        print "Usage: python main.py [theta]"
