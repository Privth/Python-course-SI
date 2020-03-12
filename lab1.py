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



