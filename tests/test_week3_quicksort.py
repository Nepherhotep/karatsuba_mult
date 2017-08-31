from unittest import TestCase

from week3_quicksort import quicksort


class TestMult(TestCase):
    def test_quicksort1(self):
        a = [7, 3, 2, 8, 6, 5, 4, 1, 9, 0]

        quicksort(a)

        self.assertEqual(a, list(range(10)))

    def test_quicksort2(self):
        a = [9, 5, 4, 7, 0, 2, 8, 6, 3, 1]

        quicksort(a)

        self.assertEqual(a, list(range(10)))
