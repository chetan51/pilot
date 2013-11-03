class MockDrone():

    def __init__(self):
        self.speed = 0.0
        self.navdata = {0: {'altitude': 0.0, 'vy': 0.0}}

    def set_speed(self, speed):
        self.speed = speed

    def land(self):
        print 'called land'
