from unittest import TestCase

import numpy

from tools import array_to_int
from week1_introduction import simple_mult, simple_mult_as_arrays


class TestMult(TestCase):
    def test_simple_mult(self):
        a, b = 123, 357

        result = simple_mult(a, b, size=4)
        assert result == a * b, result

    def test_simple_mult2(self):
        a, b = 77771232346123, 832409801237

        result = simple_mult(a, b)
        assert result == a * b, result

    def test_result_offset(self):

        a = numpy.array([2])
        b = numpy.array([2])

        result = numpy.array([0, 0])

        out = array_to_int(simple_mult_as_arrays(a, b, result, result_offset=1))

        assert out == 40, out
