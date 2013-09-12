def basic_pid(theta, thetadot, theta_int):
	# control stuff
	kp = 222                 
	kd = 11
	ki = 666
	return kp*theta + kd*thetadot + ki*theta_int
	


