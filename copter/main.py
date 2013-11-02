# !/usr/bin/env python
import sys

from logger.csv_logger import CsvLogger
from logger.console_logger import ConsoleLogger

from copter.world.copter_world import CopterWorld
from copter.controller.copter_pid_controller import CopterPIDController
from copter.controller.copter_cla_controller import CopterCLAController
from copter.predictor.copter_speed_predictor import CopterSpeedPredictor
from copter.config import logger_config, predictor_config


WORLD_BOUND = 500.
ITERATIONS_PER_RUN = 2000


def run(y, t, log_path):
    world = CopterWorld()
    controller = CopterPIDController(None)
    # controller = CopterCLAController(None)
    predictor = CopterSpeedPredictor(predictor_config)

    loggers = []
    loggers.append(CsvLogger(logger_config, log_path))
    loggers.append(ConsoleLogger(logger_config))

    state = world.observe()
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
        action = controller.act(state, predictor)
        prediction = predictor.learn(state, action)

        for logger in loggers:
            logger.log(state, action, prediction)

        world.tick(action)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 2:
        y = float(args[1])
        t = float(args[2])
        log_path = args[3] if len(args) > 3 else None
        run(y, t, log_path)
    else:
        print "Usage: python copter_main.py [y] [target_y] [log_path]"
