from unittest import TestCase

from week3_quicksort import quicksort


class TestMult(TestCase):
    def test_quicksort1(self):
        a = [7, 3, 2, 1, 6, 5, 4, 8, 9, 0]
        quicksort(a)

        self.assertEqual(a, list(range(10)))
