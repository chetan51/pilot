# !/usr/bin/env python

import sys
from config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_stabilizing_controller import PendulumStabilizingController
from pendulum.pendulum_training_controller import PendulumTrainingController
from pendulum.pendulum_predictor import PendulumPredictor
from logger.csv_logger import CsvLogger


def run(theta, controller_type, log_path):
    world = PendulumWorld()
    controller = PendulumTrainingController(
        None) if controller_type == '--train' else PendulumStabilizingController(None)
    predictor = PendulumPredictor(predictor_config['serialization'])
    state = world.observe()

    logger_config['path'] = log_path
    logger = CsvLogger(logger_config)

    world.state['theta'] = np.deg2rad(theta)

    while True:
        state = world.observe()

        predictor.disableLearning()
        force = controller.act(state, predictor)
        predictor.enableLearning()

        predicted_state = predictor.learn(state, force)

        logger.log(state, force, predicted_state)

        printTimestep(state, force, predicted_state)
        world.tick(force)


def printTimestep(state, force, predicted_state):
    print colored("[observed]  angle: " + to_str(np.rad2deg(state['theta'])) + "\t" + "position: " + to_str(state['x']) + "\t" + "force: " + to_str(force['x']), 'green')
    print colored("[predicted] angle: " + to_str(np.rad2deg(predicted_state['theta'])), 'red')


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    if len(sys.argv) > 1:
        theta = int(sys.argv[1])
        if len(sys.argv) > 3:
            controller_type = sys.argv[2] if len(sys.argv) > 2 else None
            log_path = sys.argv[3] if len(sys.argv) > 3 else None
        log_path = sys.argv[2] if len(sys.argv) > 2 else None
        controller_type = None
        run(theta, log_path, controller_type)
    else:
        print "Usage: python main.py [theta] [controller_type] [log_path]"
