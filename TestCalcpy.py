import unittest
from CALCPY import *

class TescCalcpy(unittest.TestCase):
    def test_format_input_numeric(self):
        self.assertEqual(format_input_numeric("3"), 3.0)
        self.assertEqual(format_input_numeric("3.1"), 3.1)
        self.assertEqual(format_input_numeric("4,2"), 4.2)
