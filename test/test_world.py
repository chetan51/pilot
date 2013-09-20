from pendulum.pendulum_world import PendulumWorld
import numpy as np
import sys

state = dict()
state['x'] 			= 0.
state['xdot'] 		= 0.
state['xdotdot']	= 0.
state['theta_int'] 	= 0.
state['theta'] 		= 0.174
state['thetadot'] 	= 0.
state['thetadotdot']= 0.

dt = 0.01

params = dict()
params['m'] 		= 1.
params['k'] 		= 2.
params['l'] 		= 1


ip = PendulumWorld(state, dt, params)

force = dict()
force['x'] = 0;

time_steps = sys.argv[1]

i = 0
while i < time_steps or time_steps == -1:
	print state['theta'] * 180 / np.pi
	ip.tick(force)
	i += 1