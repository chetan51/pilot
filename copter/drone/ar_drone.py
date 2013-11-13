from copter.drone.drone import Drone
from external.libardrone import libardrone
import time


class ARDrone(Drone):

    def __init__(self):
        Drone.__init__(self)
        self.drone = libardrone.ARDrone()
        print "Drone initializing..."
        time.sleep(5.)
        print "Drone initialized."

    def altitude(self):
        state = self.drone.navdata
        altitude = state[0]['altitude']
        print "Drone altitude: " + str(altitude)
        return altitude

    def speed(self):
        state = self.drone.navdata
        speed = state[0]['vy']
        print "Drone speed: " + str(speed)
        return speed

    def setSpeed(self, speed):
        self.drone.set_speed(abs(speed))
        if speed > 0:
            print "Drone moving up with speed: " + str(speed)
            self.drone.move_up()
        else:
            print "Drone moving down with speed: " + str(speed)
            self.drone.move_down()

    def takeoff(self):
        print "Drone taking off..."
        self.drone.takeoff()
        time.sleep(5.0)
        self.lowerHover()
        print "Drone took off."

    def lowerHover(self):
        self.drone.set_speed(0.3)
        self.drone.move_down()
        time.sleep(3.0)
        self.drone.hover()

    def land(self):
        print 'Drone landing...'
        self.drone.land()
        time.sleep(10.)
        print 'Drone landed.'
