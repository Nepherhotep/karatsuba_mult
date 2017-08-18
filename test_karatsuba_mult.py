from unittest import TestCase

import numpy as np

from karatsuba_mult import int_to_array


class IntToArrayTest(TestCase):
    def test_completing_with_zeros(self):
        value = int_to_array(1234, size=8)

        assert np.array_equal(value, np.array([4, 3, 2, 1, 0, 0, 0, 0]))

    def test_full_size(self):
        value = int_to_array(1234, size=4)

        assert np.array_equal(value, np.array([4, 3, 2, 1]))
