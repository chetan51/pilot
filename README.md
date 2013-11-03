# Pilot

An AI running on NuPIC using the CLA to control physical dynamic systems using goal-oriented behavior.

To install:

    pip install -r requirements.txt

To test the copter simulation:

    cd path/to/pilot
    python copter/main.py --controller [controller_name] [init_y] [target_y]

To train:
	
    cd path/to/pilot
    python copter/main.py --learn --controller PID [init_y] [target_y]

To test the CLA controller:
	
    cd path/to/pilot
    python copter/main.py --controller CLA [init_y] [target_y]

...where 

    [controller_name] = {PID, CLA}
    [init_y]          = initial altitude (float)
    [target_y]        = the target altitude (float)

## Todo

* Refactor plotters
