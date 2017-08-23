from unittest import TestCase

from calc_inversions import calc_inversions


class TestMult(TestCase):
    def test_calc_inversions(self):
        a = [1, 2, 7, 4, 5, 6, 3, 8]

        inv, result = calc_inversions(a)

        self.assertEqual(inv, 7)
        self.assertEqual(result, list(range(1, 9)))

    def test_calc_inversions2(self):
        a = [1, 2, 4, 3]

        inv, result = calc_inversions(a)

        self.assertEqual(inv, 1)
        self.assertEqual(result, [1, 2, 3, 4])

