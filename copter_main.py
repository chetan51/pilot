# !/usr/bin/env python
import os
import sys
from copter_config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from copter.copter_world import CopterWorld
from copter.copter_pid_controller import CopterPIDController
from copter.copter_ideal_predictor import CopterIdealPredictor
from logger.csv_logger import CsvLogger

WORLD_BOUND = 1000.


def run(y, t, log_path):
    world = CopterWorld()
    controller = CopterPIDController(None)
    predictor = CopterIdealPredictor(predictor_config['serialization'],
                                     world=world)
    state = world.observe()

    logger_config['path'] = os.path.abspath(log_path) if log_path else None
    logger = CsvLogger(logger_config)

    world.state['y'] = y
    controller.setTarget(t)

    while True:
        if (state['y'] > WORLD_BOUND or state['y'] < - WORLD_BOUND):
            print "Hit bounds, resetting state..."
            world.resetState()
            predictor.resetState()
            controller.resetState()

        state = world.observe()

        predictor.disableLearning()
        force = controller.act(state, predictor)
        predictor.enableLearning()

        predicted_state = predictor.learn(state, force)

        logger.log(state, force, predicted_state)

        printTimestep(state, force, predicted_state)
        world.tick(force)


def printTimestep(state, force, predicted_state):
    print colored("[observed]  dy: " + to_str(state['dy']) + "\t" + "y: " + to_str(state['y']) + "\t" + "ydot: " + to_str(state['ydot']) + "\t" + "ydotdot: " + to_str(state['ydotdot']) + "\t" + "force: " + to_str(force['y']), 'green')
    print colored("[predicted] dy: " + to_str(predicted_state['dy']), 'red')


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        y = int(args[1])
        t = int(args[2])
        log_path = args[3] if len(args) > 3 else None
        run(y, t, log_path)
    else:
        print "Usage: python copter_main.py [y] [target_y] [log_path]"
