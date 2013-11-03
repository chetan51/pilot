from copter.drone.drone import Drone
import time


class MockDrone(Drone):

    def __init__(self):
        Drone.__init__(self)
        self.disabled = False
        self.navdata = {0: {'altitude': 0.0, 'vy': 0.0}}
        print "Mock drone initializing..."
        time.sleep(3.)
        print "Mock drone initialized."

    def altitude(self):
        return self.navdata[0]['altitude']

    def speed(self):
        return self.navdata[0]['vy']

    def setSpeed(self, speed):
        if self.disabled:
            return

        self.navdata[0]['altitude'] += 0.1

    def takeoff(self):
        print "Mock drone taking off..."
        self.disabled = False
        time.sleep(3.)
        print "Mock drone took off."

    def land(self):
        print 'Mock drone landing...'
        self.disabled = True
        self.navdata[0]['altitude'] = 0
        time.sleep(3.)
        print 'Mock drone landed.'
