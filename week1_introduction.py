import numpy
import matplotlib.pyplot as plt

from tools import TickProfiler, int_to_array, array_to_int


def mult(a, b, profiler=None):
    assert a < 10 or b < 10

    if profiler:
        profiler.tick('mult')

    return a * b


def inc_value(arr, pos, value, profiler=None):
    if value:
        value += arr[pos]

        mod = int(value / 10)
        rem = value % 10

        arr[pos] = rem

        if profiler:
            profiler.tick('inc')

        inc_value(arr, pos + 1, mod)


def simple_mult(a, b, size=64, profiler=None):
    a_arr, b_arr = int_to_array(a, size), int_to_array(b, size)
    result_arr = numpy.zeros(len(a_arr) + len(b_arr), dtype=int)
    return array_to_int(simple_mult_as_arrays(a_arr, b_arr, result_arr, profiler))


def simple_mult_as_arrays(a_arr, b_arr, result_arr, a_slice=None, b_slice=None, result_offset=0, profiler=None):
    a_from, a_to = unpack_slice(a_arr, a_slice)
    b_from, b_to = unpack_slice(b_arr, b_slice)

    for a_pos in range(a_from, a_to):
        for b_pos in range(b_from, b_to):
            a_item = a_arr[a_pos]
            b_item = b_arr[b_pos]
            pos = result_offset + a_pos + b_pos - a_from - b_from
            value = mult(a_item, b_item, profiler)

            inc_value(result_arr, pos, value, profiler)
    return result_arr


def unpack_slice(a_arr, a_slice):
    if a_slice:
        a_from, a_to = a_slice
    else:
        a_from, a_to = (0, len(a_arr))
    return a_from, a_to


def karatsuba_mult(x, y, profiler=None):
    if x < 10 or y < 10:
        return mult(x, y, profiler=profiler)
    else:
        n = max(len(str(x)), len(str(y)))
        m = int(n / 2)

        a = int(x / 10 ** m)
        b = int(x % 10 ** m)
        c = int(y / 10 ** m)
        d = int(y % 10 ** m)

        step1 = karatsuba_mult(a, c)
        step2 = karatsuba_mult(b, d)
        step3 = karatsuba_mult(a + b, c + d)
        step4 = step3 - step2 - step1

        return int(step1 * 10 ** (2 * m)) + int((step4 * 10 ** m)) + step2


def main():

    sizes = range(2, 30)
    totals = []
    for size in sizes:
        a = int(size * '5')
        b = int(size * '8')

        p = TickProfiler()

        simple_mult(a, b, profiler=p, size=size)

        totals.append(p.get_total())
        print('Size {}: {} total ticks'.format(size, p.get_total()))

    plt.plot(sizes, totals)
    plt.show()

if __name__ == '__main__':
    main()