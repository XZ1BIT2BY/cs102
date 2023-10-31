import unittest
from src.lab1.calculator import addition, subtraction, multiplication, division

class TestCalculatorFunctions(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 2), 3)
        
    def test_multiplication(self):
        self.assertEqual(multiplication(4, 3), 12)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(8, 4), 2)

