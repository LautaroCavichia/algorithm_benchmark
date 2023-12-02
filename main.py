import algorithm_benchmark
from sorting_algorithms import *
from data_plotting import plot_data

for i in range(1, 1000):
    algorithm_benchmark.algorithm_benchmark(insertion_sort, i, 1)

plot_data("insertion_sort_data.csv","Insertion Sort", "Input Size", "Average Time")


for j in range(1, 1000):
    algorithm_benchmark.algorithm_benchmark(quick_sort, j, 1)

plot_data("quick_sort_data.csv","Quick Sort", "Input Size", "Average Time")

for k in range(1, 1000):
    algorithm_benchmark.algorithm_benchmark(randomized_quick_sort, k, 1)

plot_data("randomized_quick_sort_data.csv","Randomized Quick Sort", "Input Size", "Average Time")

for j in range(1, 1000):
    algorithm_benchmark.algorithm_benchmark(merge_sort, j, 1, True)

plot_data("merge_sort_data.csv","Merge Sort(ordered)", "Input Size", "Average Time")
