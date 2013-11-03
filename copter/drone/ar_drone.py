from copter.drone.drone import Drone
import libardrone
import time


class ARDrone(Drone):

    def __init__(self):
        Drone.__init__(self)
        self.drone = libardrone.ARDrone()
        print "Drone initializing..."
        time.sleep(10.)
        print "Drone initialized."

    def altitude(self):
        state = self.drone.navdata
        return state[0]['altitude']

    def speed(self):
        state = self.drone.navdata
        return state[0]['vy']

    def setSpeed(self, speed):
        self.drone.set_speed(abs(sy))
        if speed > 0:
            self.drone.move_up()
        else:
            self.drone.move_down()

    def takeoff(self):
        print "Drone taking off..."
        self.drone.takeoff()
        time.sleep(10.)
        print "Drone took off."

    def land(self):
        print 'Drone landing...'
        self.drone.land()
        time.sleep(15.)
        print 'Drone landed.'
