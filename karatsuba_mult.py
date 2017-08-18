import numpy


def int_to_array(value, size=64):
    """
    Convert integer into little-endian array
    :param value: integer
    :param size: length of array (should be power of 2)
    :return: array
    """
    arr = numpy.zeros(size, dtype=int)
    for i, c in enumerate(str(value)[::-1]):
        arr[i] = int(c)
    return arr


def array_to_int(value):
    """
    Convert little-endian array into integer
    :param value: array
    :return: int
    """
    result = ''.join(map(str, value))
    result = result[::-1]
    result = result.lstrip('0')
    return int(result)


def mult(a, b):
    assert a < 10
    assert b < 10
    return a * b


def karatsuba_mult(value1, from1, to1, value2, from2, to2):
    if from1 - to1 == 2:
        a = value1[from1]
        b = value1[to1]
        c = value2[from1]
        d = value2[to1]


def main():
    arr1 = int_to_array(123)
    arr2 = int_to_array(3335)
    print(arr1)
    print(arr2)


if __name__ == '__main__':
    main()