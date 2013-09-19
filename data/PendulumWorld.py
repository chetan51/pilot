import numpy as np
from World import *

class PendulumWorld(World):

	def tick(self, force):
		# set parameters of pendulum
		g = 9.81
		dt = self.dt
		locals().update(self.params)
		M = k*m
		push = force['controller_push']
		# set intial condition
		locals().update(self.state)

		# update accelerations
		xdotdot = (np.sin(theta)/(k+1-np.cos(theta)**2))*(g*np.cos(theta) - l*thetadot**2) - push;
		thetadotdot = (xdotdot*np.cos(theta) + g*np.sin(theta))/l

		# integrate 
		thetadot = thetadot + thetadotdot*dt
		theta = theta + thetadot*dt
		theta_int = theta_int + theta*dt

		xdot = xdot + xdotdot*dt
		x = x + xdot*dt

		# put all the variables back into the self.state
		for k,v in locals():
			if k in self.state.keys:
				self.state[k] = eval(k)




	    





