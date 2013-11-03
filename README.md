# Pilot

An AI running on NuPIC using the CLA to control physical dynamic systems using goal-oriented behavior.

## Installation

Install dependencies:

    pip install -r requirements.txt

## Running

    cd path/to/pilot

Run the Copter simulation, having the PID controller fly the copter from altitude 0 to altitude 10, with the CLA watching and learning:

    python copter/main.py 0 10 --learn

Then, run the Copter simulation using the trained CLA from the last step to directly control the copter (with learning disabled):

    python copter/main.py 0 10 --controller CLA

If you have an AR.Drone, fly the drone using a PID controller, with the CLA watching:

    python copter/main.py 0 1000 --world drone --guard drone --drone ar_drone --learn

Then, have the trained CLA directly control the AR.Drone (with learning disabled):

    python copter/main.py 0 1000 --world drone --guard drone --drone ar_drone --controller CLA

## Todo

* Refactor plotters
