import unittest
from CALCPY import *

class TestCalcpy(unittest.TestCase):
    def test_format_input_numeric(self):
        self.assertEqual(format_input_numeric("3"), 3.0)
        self.assertEqual(format_input_numeric("3.1"), 3.1)
        self.assertEqual(format_input_numeric("4,2"), 4.2)
        
    def test_is_value_valid(self):
        self.assertEqual(is_value_valid("0"), False)
        self.assertEqual(is_value_valid("1"), True)
        self.assertEqual(is_value_valid("250"), True)
        self.assertEqual(is_value_valid("-1"), False)
        
    def test_is_yes(self):
        self.assertEqual(is_yes("y"), True)
        self.assertEqual(is_yes("Y"), True)
        self.assertEqual(is_yes("o"), False)
        self.assertEqual(is_yes("F"), False)
        self.assertEqual(is_yes("N"), False)
