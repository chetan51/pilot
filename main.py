# !/usr/bin/env python
import os
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
        None) if controller_type == 't' else PendulumStabilizingController(None)
    predictor = PendulumPredictor(predictor_config['serialization'])
    state = world.observe()

    logger_config['path'] = os.path.abspath(log_path) if log_path else None
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
    args = sys.argv
    if len(args) > 1:
        theta = int(args[1])
        controller_type = 't' if '--train' in args else 's'
        log_path = sys.argv[3] if len(sys.argv) > 3 else None
        run(theta, controller_type, log_path)
    else:
        print "Usage: python main.py [theta] [controller_type] [log_path]"
