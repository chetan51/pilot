from PendulumWorld import *

state = dict()
state['x'] 			= 0.
state['xdot'] 		= 0.
state['xdotdot']	= 0.
state['theta_int'] 	= 0.
state['theta'] 		= 3.14
state['thetadot'] 	= 0.
state['thetadotdot']= 0.

params = dict()
params['m'] 		= 1.
params['k'] 		= 2.
params['l'] 		= 1

dt = 0.01
ip = PendulumWorld(state, dt, params)

force = dict()
force['controller_push'] = 0;

for i in range(10000):
	print state['theta']
	ip.tick(force)

