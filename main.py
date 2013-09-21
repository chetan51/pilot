#!/usr/bin/env python

import sys
import numpy as np
from core.predictor import Predictor
from pendulum.pendulum_world import PendulumWorld
from pendulum.pendulum_controller import PendulumController

def run(theta):
    state = {   'x'             : 0.,
                'xdot'          : 0.,
                'xdotdot'       : 0.,
                'theta_int'     : 0.,
                'theta'         : np.deg2rad(theta),
                'thetadot'      : 0.,
                'thetadotdot'   : 0.}

    dt = 0.01

    params = {  'm'             : 1.,
                'k'             : 2.,
                'l'             : 1.}

    world = PendulumWorld(state, dt, params)
    controller = PendulumController(None)
    predictor = Predictor()

    while True:
        state = world.observe()
        print state

        predictor.disableLearning()
        force = controller.act(state, predictor)
        print force
        
        predictor.enableLearning()
        predictor.learn(state, force)

        world.tick(force)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    theta = int(sys.argv[1])
    run(theta)
  else:
    print "Usage: python main.py [theta]"
