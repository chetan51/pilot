class MockDrone():

    def __init__(self):
        self.speed = 0.0
        self.disabled = False
        self.navdata = {0: {'altitude': 0.0, 'vy': 0.0}}

    def set_speed(self, speed):
        if self.disabled:
            return

        self.speed = speed
        self.navdata[0]['altitude'] += 0.1

    def takeoff(self):
        print "Mock drone taking off..."
        self.disabled = False

    def land(self):
        print 'Mock drone landing...'
        self.disabled = True
        self.navdata[0]['altitude'] = 0
