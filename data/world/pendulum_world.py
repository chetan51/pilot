import numpy as np
from world import *

class PendulumWorld(World):

	def tick(self, force):
		# set parameters of pendulum
		g = 9.81
		dt = self.dt
		# locals().update(self.params)
		
		push = force['controller_push']
		# set intial condition
		# locals().update(self.state)
		s = self.state
		p = self.params
		
		[x, xdot, xdotdot, theta_int, theta, thetadot, thetadotdot] = [s['x'], s['xdot'], s['xdotdot'], s['theta_int'], s['theta'], s['thetadot'], s['thetadotdot']]
		[m,k,l] = [p['m'], p['k'], p['l']]
		

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
		[s['x'], s['xdot'], s['xdotdot'], s['theta_int'], s['theta'], s['thetadot'], s['thetadotdot']] = [x, xdot, xdotdot, theta_int, theta, thetadot, thetadotdot]









