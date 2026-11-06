import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        self.assertEqual(self.calc.add(3, 7), 10)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
if __name__ == "_main_":
    unittest.main()