import time
import random
from data_export import export_to_csv
from data_plotting import plot_data


def algorithm_benchmark(algorithm, input_size, trials):
    times = []
    for i in range(trials):
        lst = [random.randint(0, input_size) for i in range(input_size)]
        start = time.time()
        algorithm(lst)
        end = time.time()
        times.append(end-start)
        export_to_csv(times, f"{algorithm.__name__}_data.csv", input_size)

    return sum(times)/trials
