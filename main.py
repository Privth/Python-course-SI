from onsets import onsets
from sorting_methods import generate_random_numbers, bubble_sort, insertion_sort
from time_counter import time_compare

threshold = 5656
data = [generate_random_numbers(10, 1, 31310), threshold]


print(time_compare(onsets, data))

