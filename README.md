# Pilot

An AI running on NuPIC using the CLA to control physical dynamic systems using goal-oriented behavior.

To test the pendulum simulation:
	cd path/to/pilot
	python test.py theta n

where 'theta' is the initial angle offset in degrees (0 degrees is the desired state)
and 'n' is the number of steps to run the simulation
if n is set to -1, then the simulation runs forever