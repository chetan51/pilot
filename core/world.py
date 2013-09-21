class World:
    
	def __init__(self, state, dt, params):
		self.state = state
		self.dt = dt
		self.params = params

	def observe(self):
		return self.state

	def tick(self, force):
		print "Tick is not specified" 