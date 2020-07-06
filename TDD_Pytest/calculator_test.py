import pytest
import unittest

from calculator import *

class Calc_Test(unittest.TestCase):

    simple_calc = Calculator()

    def test_remainder(self):
        self.assertEqual(self.simple_calc.remainder(2, 2), 0)

    def test_inches_to_cm(self):
        self.assertEqual(self.simple_calc.inches_to_cm(1), 2.54)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(2, 2), 4)
    #
    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(9, 3), 3)

# Type python -m pytest to work