import algorithm_benchmark
from insertion_sort import insertion_sort
from data_plotting import plot_data

for i in range(1, 1000):
    algorithm_benchmark.algorithm_benchmark(insertion_sort, i, 1)

plot_data("insertion_sort_data.csv","Insertion Sort", "Input Size", "Average Time")

