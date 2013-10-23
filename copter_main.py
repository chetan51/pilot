# !/usr/bin/env python
import os
import sys
from config import logger_config, predictor_config
from termcolor import colored
import numpy as np
from logger.csv_logger import CsvLogger


from copter.copter_world import CopterWorld


def run():
    world = CopterWorld()
    i = 0
    while True:
        state = world.observe()
        dy = state['dy']
        bit = 1 if dy < 0 else 0
        force = {'up': bit}
        world.tick(force)
        print dy
        i += 1

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        run()
    else:
        print "Usage: python copter_main.py"
