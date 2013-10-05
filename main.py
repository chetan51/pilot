# !/usr/bin/env python

import sys
from config import config
from termcolor import colored
import numpy as np
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_controller import PendulumController
from pendulum.pendulum_predictor import PendulumPredictor
from logger.csv_logger import CsvLogger
logger_config = config['logger']
logger_keys = logger_config['keys']


def run(theta, log_path):
    world = PendulumWorld()
    controller = PendulumController(None)
    predictor = PendulumPredictor()
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

        logger.log(dict_to_list(state, logger_keys['state']) +
                   dict_to_list(force, logger_keys['force']) +
                   dict_to_list(predicted_state, logger_keys['predicted_state']))

        printTimestep(state, force, predicted_state)
        world.tick(force)


def printTimestep(state, force, predicted_state):
    print colored("[observed]  angle: " + to_str(np.rad2deg(state['theta'])) + "\t" + "position: " + to_str(state['x']) + "\t" + "force: " + to_str(force['x']), 'green')
    print colored("[predicted] angle: " + to_str(np.rad2deg(predicted_state['theta'])), 'red')


def to_str(f):
    return "%.2f" % f


def dict_to_list(dict, keys):
    return map((lambda x: dict[x]), keys)


if __name__ == "__main__":
    log = False
    if len(sys.argv) > 1:
        theta = int(sys.argv[1])
        log_path = sys.argv[2] if len(sys.argv) > 2 else None
        run(theta, log_path)
    else:
        print "Usage: python main.py [theta]"
