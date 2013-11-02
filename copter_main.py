# !/usr/bin/env python
import os
import sys
from copter_config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from copter.copter_world import CopterWorld
from copter.copter_pid_controller import CopterPIDController
from copter.copter_cla_controller import CopterCLAController
from copter.copter_speed_predictor import CopterSpeedPredictor
from logger.csv_logger import CsvLogger

WORLD_BOUND = 500.
ITERATIONS_PER_RUN = 2000


def run(y, t, log_path):
    world = CopterWorld()
    controller = CopterPIDController(None)
    # controller = CopterCLAController(None)
    predictor = CopterSpeedPredictor(predictor_config['serialization'])

    state = world.observe()

    logger_config['path'] = os.path.abspath(log_path) if log_path else None
    logger = CsvLogger(logger_config)

    world.state['y'] = y

    controller.setTarget(t)
    predictor.setTarget(t)

    i = 0
    run = 0
    while True:
        i += 1

        if (i % ITERATIONS_PER_RUN == 0 or state['y'] > WORLD_BOUND or state['y'] < - WORLD_BOUND):
            run += 1
            print "Resetting. Entering run: " + str(run)
            world.resetState()
            predictor.resetState()
            controller.resetState()

        state = world.observe()
        speed = controller.act(state, predictor)
        prediction = predictor.learn(state, speed)

        logger.log(state, speed, prediction)

        printTimestep(state, speed, prediction)
        world.tick(speed)


def printTimestep(state, speed, prediction):
    print colored("[observed]  y: " + to_str(state['y']) + "\t" + "ydot: " + to_str(state['ydot']) + "\t" + "\t" + "speed input: " + to_str(speed['y']), 'green')
    print colored("[predicted] speed_y: " + to_str(prediction.values()[0]), 'red')


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
