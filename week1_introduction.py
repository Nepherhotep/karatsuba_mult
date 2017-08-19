import numpy

from tools import TickProfiler


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


def mult(a, b, profiler=None):
    assert a < 10
    assert b < 10

    if profiler:
        profiler.tick()

    return a * b


def inc_value(arr, pos, value, profiler=None):
    if value:
        value += arr[pos]

        mod = int(value / 10)
        rem = value % 10

        arr[pos] = rem

        if profiler:
            profiler.tick()

        inc_value(arr, pos + 1, mod)


def simple_mult(a, b, size=64, profiler=None):
    a_arr, b_arr = int_to_array(a, size), int_to_array(b, size)
    return array_to_int(simple_mult_as_arrays(a_arr, b_arr, profiler))


def simple_mult_as_arrays(a_arr, b_arr, profiler=None):
    result = numpy.zeros(len(a_arr) + len(b_arr), dtype=int)
    for a_pos, a_item in enumerate(a_arr):
        for b_pos, b_item in enumerate(b_arr):
            pos = a_pos + b_pos
            value = mult(a_item, b_item, profiler)

            inc_value(result, pos, value, profiler)
    return result


def karatsuba_mult(value1, from1, to1, value2, from2, to2):
    if from1 - to1 == 2:
        a = value1[from1]
        b = value1[to1]
        c = value2[from1]
        d = value2[to1]

        step1 = mult(a, c)
        step2 = mult(b, d)
        step3 = (a + b) * (c + d)
        step4 = step3 - step2 - step1


def main():

    for i in range(1, 6):
        size = 2 ** i

        p = TickProfiler()

        a = int(size * '2')
        b = int(size * '7')

        simple_mult(a, b, profiler=p, size=size)
        print('Size {}: {} ticks'.format(size, p.get_ticks()))


if __name__ == '__main__':
    main()