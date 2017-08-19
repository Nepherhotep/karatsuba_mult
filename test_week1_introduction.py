from unittest import TestCase

import numpy as np

from week1_introduction import int_to_array, array_to_int, simple_mult


class IntToArrayTest(TestCase):
    def test_int_to_array_completing_with_zeros(self):
        value = int_to_array(1234, size=8)

        assert np.array_equal(value, np.array([4, 3, 2, 1, 0, 0, 0, 0]))

    def test_int_to_array_full_size(self):
        value = int_to_array(1234, size=4)

        assert np.array_equal(value, np.array([4, 3, 2, 1]))

    def test_array_to_int(self):
        value = array_to_int(np.array([4, 3, 2, 1]))

        assert value == 1234, value

    def test_array_to_int_with_zeros(self):
        value = array_to_int(np.array([0, 4, 3, 2, 1, 0, 0, 0, 0]))

        assert value == 12340, value


class TestMult(TestCase):
    def test_simple_mult(self):
        a, b = 123, 357

        result = simple_mult(a, b, size=4)
        assert result == a * b, result

    def test_simle_mult2(self):
        a, b = 77771232346123, 832409801237

        result = simple_mult(a, b)
        assert result == a * b, result
