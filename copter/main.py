# !/usr/bin/env python
import argparse

from core.runner import Runner

from logger.csv_logger import CsvLogger
from logger.console_logger import ConsoleLogger

from copter.world.copter_world import CopterWorld
from copter.controller.copter_pid_controller import CopterPIDController
from copter.controller.copter_cla_controller import CopterCLAController
from copter.predictor.copter_speed_predictor import CopterSpeedPredictor
from copter.config import runner_config, logger_config, predictor_config, world_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('init_y', type=int, help='starting y position')
    parser.add_argument('target_y', type=int, help='target y position')
    parser.add_argument('--log', help='path to log file')
    parser.add_argument('--learn', action='store_const', const=True,
                        help='enable learning')
    parser.add_argument('--controller',
                        help='controller type',
                        choices=['PID', 'CLA'],
                        default="PID")

    args = parser.parse_args()

    world = CopterWorld(world_config)
    predictor = CopterSpeedPredictor(predictor_config)

    if args.controller == "CLA":
        controller = CopterCLAController(None)
    else:
        controller = CopterPIDController(None)

    runner = Runner(runner_config,
                    world, predictor, controller,
                    learning_enabled=args.learn,
                    target_y=args.target_y)

    runner.addLogger(ConsoleLogger(logger_config))
    if args.log:
        runner.addLogger(CsvLogger(logger_config, args.log))

    world.setInitY(args.init_y)
    runner.setTarget(args.target_y)

    while True:
        runner.tick()
