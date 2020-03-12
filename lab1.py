from random import randrange


def generate_random_numbers(length, minimum, maximum):
    if minimum > maximum:
        print('minimum can not be bigger than maximum')
        return
    if length == 0:
        print('length can not be equal to zero')
        return

    array = []
    for i in range(length):
        array.append(randrange(minimum, maximum))

    return array


def bubble_sort(array):
    if len(array) == 0:
        return print('array length can not be equal to 0')

    length = len(array)
    for i in range(length):
        swapped = False

        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

        return array
