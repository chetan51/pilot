# !/usr/bin/env python
import os
import sys
from copter_config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from copter.copter_world import CopterWorld
from copter.copter_pid_controller import CopterPIDController
from copter.copter_cla_controller import CopterCLAController
from copter.copter_force_predictor import CopterForcePredictor
from logger.csv_logger import CsvLogger

WORLD_BOUND = 1000.
ITERATIONS_PER_RUN = 5000


def run(y, t, log_path):
    world = CopterWorld()
    controller = CopterPIDController(None)
    # controller = CopterCLAController(None)
    predictor = CopterForcePredictor(predictor_config['serialization'])

    state = world.observe()

    logger_config['path'] = os.path.abspath(log_path) if log_path else None
    logger = CsvLogger(logger_config)

    world.state['y'] = y

    controller.setTarget(t)
    predictor.setTarget(t)
    i = 0

    while True:
        i += 1

        if (i > ITERATIONS_PER_RUN or state['y'] > WORLD_BOUND or state['y'] < - WORLD_BOUND):
            print "Hit bounds, resetting state..."
            i = 0
            world.resetState()
            predictor.resetState()
            controller.resetState()

        state = world.observe()
        force = controller.act(state, predictor)
        prediction = predictor.learn(state, force)

        logger.log(state, force, prediction)

        printTimestep(state, force, prediction)
        world.tick(force)


def printTimestep(state, force, prediction):
    print colored("[observed]  y: " + to_str(state['y']) + "\t" + "ydot: " + to_str(state['ydot']) + "\t" + "ydotdot: " + to_str(state['ydotdot']) + "\t" + "force: " + to_str(force['y']), 'green')
    print colored("[predicted] force_y: " + to_str(prediction.values()[0]), 'red')


def to_str(f):
    return "%.2f" % f


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        y = float(args[1])
        t = float(args[2])
        log_path = args[3] if len(args) > 3 else None
        run(y, t, log_path)
    else:
        print "Usage: python copter_main.py [y] [target_y] [log_path]"
