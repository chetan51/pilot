# Pilot

An AI running on NuPIC using the CLA to control physical dynamic systems using goal-oriented behavior.

To install:

    pip install -r requirements.txt

To test the pendulum simulation:

    cd path/to/pilot
    python main.py [theta]

...where [theta] is the initial angle offset in degrees (0 degrees is exactly vertical).

## Todo

* Wrap theta
* Refactor loggers
* Add ConsoleLogger
* Refactor plotters
* Implement training algorithm