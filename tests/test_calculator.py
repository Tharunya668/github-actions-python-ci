import unittest
import sys
import os

# Add src directory to sys.path to import modules from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import functions from calculator module
from calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Test cases for addition function
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        # Test cases for subtraction function
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_divide(self):
        # Test cases for division function
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        # Test division by zero, should raise ValueError
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
