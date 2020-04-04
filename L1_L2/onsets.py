def onsets(data, method):
    list_of_elements = data[0]
    passed_threshold = data[1]
    numbers_bigger_than_threshold = []
    list_of_indexes = []

    print("Array: {}\n".format(list_of_elements))

    for index, value in enumerate(list_of_elements):
        print("index: {} value: {}".format(index, value))

        if value > passed_threshold:
            bigger_than_threshold = value
            numbers_bigger_than_threshold.append(bigger_than_threshold)

    print("\nnumbers_bigger_than_threshold: {}\n".format(numbers_bigger_than_threshold))

    sorted_list_desc = sorted(numbers_bigger_than_threshold, reverse=True)
    sorted_list_desc = sorted_list_desc[:3]

    print("numbers_bigger_than_threshold sorted and cut: {}\n".format(sorted_list_desc))

    for i in sorted_list_desc:
        list_of_indexes.append(list_of_elements.index(i))

    print("List of indexes: {}\n".format(list_of_indexes))
    print("passed_threshold: {}\n".format(passed_threshold))

    sorted_list = method(list_of_elements)

    print("sorted list: {}\n".format(sorted_list))

    return [list_of_indexes, sorted_list]


