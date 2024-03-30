import unittest

from src.day_002_tip_calculator.tip_calculator import calculate_tip
from utils import round_up


########################################################################################################################

class TestChallenge002(unittest.TestCase):
    def test_calculate_tip(self):
        total_bill = 124.54
        tip = 12
        people_count = 5
        result = round_up(calculate_tip(total_bill, tip, people_count), 2)
        self.assertEqual(27.90, result)


########################################################################################################################

if __name__ == '__main__':
    unittest.main()

########################################################################################################################
