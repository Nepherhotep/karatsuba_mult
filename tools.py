import numpy


class TickProfiler:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1

    def get_ticks(self):
        return self.count


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