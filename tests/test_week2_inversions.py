from unittest import TestCase

from week2_calc_inversions import calc_inversions


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

    def test_calc_inversions3(self):
        a = [1, 2, 4, 3, 5]

        inv, result = calc_inversions(a)

        self.assertEqual(inv, 1)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_calc_inversions4(self):
        a = [1, 3, 2]

        inv, result = calc_inversions(a)

        self.assertEqual(inv, 1)
        self.assertEqual(result, [1, 2, 3])


