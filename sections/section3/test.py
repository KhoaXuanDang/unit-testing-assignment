import unittest
from code.my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 10, 'The sum is wrong.')

    def test_diff(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_difference(), 6, 'The difference is wrong.')

    def test_product(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_product(), 16, 'The product is wrong.')

    def test_quotient(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_quotient(), 4, 'The quotient is wrong.')
    
    # Alternative for setUpClass - Optimal option can choose either setUpClass or setUp but not both
    # @classmethod
    # def setUpClass(self):
    #     self.calculation = Calculations(8, 2)

    # def setUp(self):
    #     self.calculation = Calculations(8, 2)

    # def test_sum(self):
    #     self.assertEqual(self.calculation.get_sum(), 10, 'The sum is wrong.')

    # def test_diff(self):
    #     self.assertEqual(self.calculation.get_difference(), 6, 'The difference is wrong.')

    # def test_product(self):
    #     self.assertEqual(self.calculation.get_product(), 16, 'The product is wrong.')

    # def test_quotient(self):
    #     self.assertEqual(self.calculation.get_quotient(), 4, 'The quotient is wrong.')
if __name__ == '__main__':
    unittest.main()