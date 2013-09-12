import numpy as np
import matplotlib.pyplot as plt
import controllers as ctrl

# Constants
m = 1                  	# mass of pendulum (kg) MADE UP
M = 0.0226796*2        	# mass of wheels (kg) MADE UP
g = 9.81               	# acceleration of gravity (m/s/s) MADE UP
l = 0.2286             	# length of inverted pendulum
tfinal = 2            	# total time of simulation
dt = .0001             	# time step 
t = np.linspace(0,tfinal, tfinal/dt)    # time vector of simulation 

# initial values of state
x = 0                 	# translational displacement of system (in perspective of wheels)
xdot = 0               	# change in x
xdotdot = 0            	# change in xdot

theta_int = 0         	# theta integrated
theta = 1*np.pi/180     # deviation angle of inverted pendulum (radians)
thetadot = 0         	# change in theta
thetadotdot = 0       	# change in thetadot

control_force = ctrl.basic_pid(theta,thetadot,theta_int)
# current = kp*theta + kd*thetadot + ki*theta_int;    # control effort for torque in wheels

# recording stuff
state = np.zeros([2,np.size(t)+1])
state[0][0] = theta
state[1][0] = x

# integration loop
for i in range(np.size(t)):
    # set change of state values
    Meq = M+m*np.sin(theta)**2
    xdotdot = (-control_force - m*np.sin(theta)*(l*thetadot**2 - g*np.cos(theta)) )/Meq
    thetadotdot = (xdotdot*np.cos(theta) + g*np.sin(theta))/l
    thetadot = thetadot + thetadotdot*dt
    
    # integrate 
    xdot = xdot + xdotdot*dt
    theta = theta + thetadot*dt
    x = x + xdot*dt
    theta_int = theta_int + theta*dt
    
    # record data
    state[0][i+1] = theta;
    state[1][i+1] = x;

    # control stuff
    control_force = ctrl.basic_pid(theta,thetadot,theta_int)

print np.shape(state[0][0:-1])
print np.shape(t)
plt.figure(1)
plt.plot(t,state[0][0:-1])
plt.ylabel('theta(radians)')
plt.xlabel('time(s)')
plt.title('Theta vs Time')

plt.figure(2)
plt.plot(t,state[1][0:-1])
plt.ylabel('X(meters)')
plt.xlabel('time(s)')
plt.title('X vs Time')
plt.show()