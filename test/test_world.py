from pendulum.pendulum_world import PendulumWorld
import numpy as np
import sys

theta = int(sys.argv[1])
time_steps = int(sys.argv[2])

state = dict()
state['x'] 			= 0.
state['xdot'] 		= 0.
state['xdotdot']	= 0.
state['theta_int'] 	= 0.
state['theta'] 		= np.deg2rad(theta)
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



i = 0
while i < time_steps or time_steps == -1:
	print np.rad2deg(state['theta'])
	ip.tick(force)
	i += 1