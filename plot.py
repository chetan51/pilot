from plotter.plot import csv_plot
import sys

if __name__ == "__main__":
    print len(sys.argv)
    if len(sys.argv) >= 2:
        log_path = sys.argv[1]
        field_names = sys.argv[2:]
        csv_plot(log_path, field_names)
    else:
        print "Usage: python plot.py [path/to/log] [field names]"
