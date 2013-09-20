from pendulum.pendulum_world import PendulumWorld
import numpy as np
import sys

theta = int(sys.argv[1])
time_steps = int(sys.argv[2])

state = {	'x' 			: 0.,
	     	'xdot' 		: 0.,
	     	'xdotdot' 		: 0.,
	     	'theta_int' 	: 0.,
	     	'theta' 		: np.deg2rad(theta),
	     	'thetadot' 	: 0.,
	     	'thetadotdot' 	: 0.}

dt = 0.01

params = {	'm' 			: 1.,
			'k'				: 2.,
			'l'				: 1.}

force = {'x' : 0}

ip = PendulumWorld(state, dt, params)

i = 0
while i < time_steps or time_steps == -1:
	print np.rad2deg(state['theta'])
	ip.tick(force)
	i += 1