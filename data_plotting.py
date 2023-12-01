import matplotlib.pyplot as plt
import csv


def plot_data(filename, title, xlabel, ylabel):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [(int(row['Input Size']), float(row['Average Time'])) for row in reader]

    x_values = [row[0] for row in data]
    y_values = [row[1] for row in data]

    plt.plot(x_values, y_values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
