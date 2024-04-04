import unittest
from math import inf

from src.day_010_calculator.calculator import run_calculation


########################################################################################################################

class TestChallenge010(unittest.TestCase):
    def test_run_calculation(self):
        self.assertEqual(2.5, run_calculation(5, 2, "/"))
        self.assertEqual(None, run_calculation(23, 2324, "asdf"))
        self.assertEqual(inf, run_calculation(5, 0, "/"))
        self.assertEqual(inf, run_calculation(0, 0, "/"))


########################################################################################################################

if __name__ == '__main__':
    unittest.main()


########################################################################################################################
