import numpy


def int_to_array(value, size=64):
    """
    Convert integer into little-endian array
    :param value: integer
    :param size: length of array (should be power of 2)
    :return:
    """
    arr = numpy.zeros(size, dtype=int)
    for i, c in enumerate(str(value)[::-1]):
        arr[i] = int(c)
    return arr


def mult(a, b):
    assert a < 10
    assert b < 10
    return a * b


def main():
    arr1 = int_to_array(123)
    arr2 = int_to_array(3335)
    print(arr1)
    print(arr2)


if __name__ == '__main__':
    main()