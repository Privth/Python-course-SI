import time
import copy
from L1_L2.sorting_methods import bubble_sort, insertion_sort


def timer(function, list_of_elements, sorting_method):
    start = time.time()
    function(list_of_elements, sorting_method)
    stop = time.time()
    total_time = stop - start

    return total_time


def time_compare(function, list_of_elements):
    copy_list_of_elements = copy.deepcopy(list_of_elements)

    times = [
        timer(function, list_of_elements, bubble_sort),
        timer(function, copy_list_of_elements, insertion_sort)
    ]

    return times
