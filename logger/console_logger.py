from logger import Logger
from termcolor import colored


class ConsoleLogger(Logger):

    def log(self, state, action, prediction):
        print colored("[observed]  y: " + self.to_str(state['y']) + "\t" + "ydot: " + self.to_str(state['ydot']) + "\t" + "\t" + "control speed_y: " + self.to_str(action['speed_y']), 'green')
        print colored("[predicted] control speed_y: " + self.to_str(prediction.values()[0]), 'red')

    """ Helpers """

    def to_str(self, f):
        return "%.2f" % f
