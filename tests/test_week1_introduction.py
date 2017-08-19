from unittest import TestCase

from week1_introduction import simple_mult


class TestMult(TestCase):
    def test_simple_mult(self):
        a, b = 123, 357

        result = simple_mult(a, b, size=4)
        assert result == a * b, result

    def test_simle_mult2(self):
        a, b = 77771232346123, 832409801237

        result = simple_mult(a, b)
        assert result == a * b, result
