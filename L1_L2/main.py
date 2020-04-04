from L1_L2.onsets import onsets
from L1_L2.sorting_methods import generate_random_numbers
from L1_L2.time_counter import time_compare


threshold = 5656
data = [generate_random_numbers(10, 1, 31310), threshold]

print(time_compare(onsets, data))

