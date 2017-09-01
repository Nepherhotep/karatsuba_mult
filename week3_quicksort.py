from tools import load_input_array


def first_element_pivot(a, from_index, to_index):
    return from_index, a[from_index]


def final_element_pivot(a, from_index, to_index):
    return to_index - 1, a[to_index - 1]


def median_element_pivot(a, from_index, to_index):
    item1 = a[from_index]

    middle = int((from_index + to_index) / 2)
    item2 = a[middle]

    item3 = a[to_index - 1]

    elements = [item1, item2, item3]
    elements.sort()

    if elements[1] == item1:
        return from_index, item1
    elif elements[1] == item2:
        return middle, item2
    else:
        return to_index - 1, item3


def quicksort(a, from_index=0, to_index=None, get_pivot_function=first_element_pivot):
    # automatically select the whole array, if nothing passed
    if to_index is None:
        to_index = len(a)

    pivot_index, pivot = get_pivot_function(a, from_index, to_index)

    # swap pivot to the first position to avoid confusion later
    swap(a, from_index, pivot_index)
    pivot_index = from_index

    last_part = from_index
    for last_seen in range(from_index, to_index):
        element = a[last_seen]
        if element <= pivot:
            swap(a, last_part, last_seen)
            last_part += 1

    # swap pivot to the last partitioned position
    swap(a, last_part - 1, pivot_index)

    # perform quick sort of the left part
    if last_part - from_index > 1:
        quicksort(a, from_index, last_part - 1)

    # perform quick sort of the right part
    if to_index - last_part > 1:
        quicksort(a, last_part, to_index)


def swap(a, index1, index2):
    if index1 > index2:
        index1, index2 = index2, index1
    # print('swap: {}, {}[{}] -> {}[{}]'.format(a, a[index1], index1, a[index2], index2))
    # print('swap: ' + '   ' * index1 + ' ^ ' + (index2 - index1 - 1) * '   ' + ' ^ ')
    a[index1], a[index2] = a[index2], a[index1]


if __name__ == '__main__':
    input_array = load_input_array('fixtures/quicksort.txt')
    quicksort(input_array)
    for item in input_array:
        print(item)

    
