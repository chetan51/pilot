# !/usr/bin/env python
import argparse
import sys

from core.runner import Runner

from logger.csv_logger import CsvLogger
from logger.console_logger import ConsoleLogger

from copter.world.copter_world import CopterWorld
from copter.world.drone_world import DroneWorld

from copter.drone.mock_drone import MockDrone
from copter.drone.ar_drone import ARDrone

from copter.controller.copter_pid_controller import CopterPIDController
from copter.controller.copter_cla_controller import CopterCLAController
from copter.controller.copter_testing_controller import CopterTestingController
from copter.predictor.copter_speed_predictor import CopterSpeedPredictor

from copter.guard.copter_guard import CopterGuard
from copter.guard.drone_guard import DroneGuard

from copter.config import runner_config, logger_config, predictor_config, world_config


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('init_y', type=int, help='starting y position')
    parser.add_argument('target_y', type=int, help='target y position')
    parser.add_argument('final_target_y', type=int,
                        help='final target y position')
    parser.add_argument('--log', help='path to log file')
    parser.add_argument('--learn', action='store_const', const=True,
                        help='enable learning')
    parser.add_argument('--controller',
                        help='controller type',
                        choices=['PID', 'CLA', 'unsupervised'],
                        default="PID")
    parser.add_argument('--world',
                        help='world type',
                        choices=['copter', 'drone'],
                        default="copter")
    parser.add_argument('--drone',
                        help='drone type',
                        choices=['ar_drone', 'mock_drone'],
                        default="mock_drone")
    parser.add_argument('--guard',
                        help='guard type',
                        choices=['copter', 'drone'])

    args = parser.parse_args()

    predictor = CopterSpeedPredictor(predictor_config)

    if args.world == "copter":
        world = CopterWorld(world_config)
    else:
        if args.drone == "ar_drone":
            drone = ARDrone()
        else:
            drone = MockDrone()

        world = DroneWorld(world_config, drone=drone)

    controller = {
        'CLA': lambda: CopterCLAController(None),
        'PID': lambda: CopterPIDController(None),
        'unsupervised': lambda: CopterTestingController(None)
    }[args.controller]()

    if args.guard == "copter":
        guard = CopterGuard()
    elif args.guard == "drone":
        guard = DroneGuard()
    else:
        guard = None

    runner = Runner(runner_config,
                    world, predictor, controller,
                    guard=guard,
                    learning_enabled=args.learn,
                    target_y=args.target_y,
                    final_target_y=args.final_target_y)

    runner.addLogger(ConsoleLogger(logger_config))
    if args.log:
        runner.addLogger(CsvLogger(logger_config, args.log))

    world.setup()
    world.setInitY(args.init_y)

    runner.newRun()

    while True:
        try:
            runner.tick()

        except Exception as e:
            print e
            runner.world.terminate()
            sys.exit()
