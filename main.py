#!/usr/bin/env python

import sys
from termcolor import colored
import numpy as np
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_controller import PendulumController
from pendulum.pendulum_predictor import PendulumPredictor


def run(theta, log_path):
    world = PendulumWorld()
    controller = PendulumController(None)
    predictor = PendulumPredictor()

    if log_path:
        log_file = prepare_log_file(log_path, world)

    world.state['theta'] = np.deg2rad(theta)

    while True:
        state = world.observe()

        predictor.disableLearning()
        force = controller.act(state, predictor)
        predictor.enableLearning()

        predicted_state = predictor.learn(state, force)

        if log_file:
            log_file.write(
                ','.join(map(str, state.values())) + ',' +
                str(force['x']) +
                '\n'
            )

        printTimestep(state, force, predicted_state)
        world.tick(force)
    if log:
        log_file.close()


def printTimestep(state, force, predicted_state):
    print colored("[observed]  angle: " + to_str(np.rad2deg(state['theta'])) + "\t" + "position: " + to_str(state['x']) + "\t" + "force: " + to_str(force['x']), 'green')
    print colored("[predicted] angle: " + to_str(np.rad2deg(predicted_state['theta'])), 'red')


def prepare_log_file(log_path, world):
    log_file = open(log_path, 'w')
    log_file.write(','.join(world.observe().keys()) + ',force' + '\n')
    log_file.write(','.join(['float' for i in xrange(8)]) + '\n')
    log_file.write(',\n')
    return log_file


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    log = False
    if len(sys.argv) > 1:
        theta = int(sys.argv[1])
        if len(sys.argv) > 2:
            log_path = sys.argv[2]
        run(theta, log_path)
    else:
        print "Usage: python main.py [theta] [path/to/log]"
