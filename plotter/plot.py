import csv
import numpy as np
import matplotlib.pyplot as plt

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def csv_plot(file_path, field_names):
    lines = [line.strip().split(',') for line in open(file_path)]
    labels = meta_process(lines[0])
    columns = []
    for i in field_names:
        columns.append(labels.index(i))
    y = np.zeros([len(field_names), len(lines)])
    x = np.arange(len(lines))
    for col in range(len(lines[3:])):
        for row in range(len(field_names)):
            y[row][col] = float(lines[3 + col][columns[row]])
    color_counter = 0
    plot_list = []
    for i in range(len(field_names)):
        plot_list.append(x)
        plot_list.append(y[i][:])
        plot_list.append(colors[color_counter])
        color_counter += 1

    plt.plot(*plot_list)
    plt.xlabel('Time Steps')
    plt.ylabel('hella fields')
    plt.legend(tuple(field_names))
    plt.show()


def meta_process(line):
    return map((lambda x: x.strip()), line)
