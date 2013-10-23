# !/usr/bin/env python
import os
import sys
from config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from copter.copter_world import CopterWorld
from copter.copter_controller import CopterController
from copter.copter_predictor import CopterPredictor
from logger.csv_logger import CsvLogger


def run(y, log_path):
    world = CopterWorld()
    controller = CopterController(None)
    predictor = CopterPredictor(predictor_config['serialization'])
    state = world.observe()

    logger_config['path'] = os.path.abspath(log_path) if log_path else None
    logger = CsvLogger(logger_config)

    world.state['y'] = y

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
    print colored("[observed]  dy: " + to_str(state['dy']) + "\t" + "ydot: " + to_str(state['ydot']) + "\t" + "ydotdot: " + to_str(state['ydotdot']) + "\t" + "force: " + to_str(force['y']), 'green')
    print colored("[predicted] dy: " + to_str(predicted_state['dy']), 'red')


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        y = int(args[1])
        log_path = sys.argv[2] if len(sys.argv) > 2 else None
        run(y, log_path)
    else:
        print "Usage: python copter_main.py [y] [log_path]"
