import unittest
from oop_calculator import Calculator

calculator = Calculator('calculator')

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(10, -5), 5)
        self.assertEqual(calculator.add(-10, -5), -15)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(10, -5), 15)
        self.assertEqual(calculator.subtract(-10, -5), -5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(10, -5), -50)
        self.assertEqual(calculator.multiply(-10, -5), 50)

    # def test_divide(self):
    #     self.assertEqual(divide(6,3), 2)
    #     self.assertEqual(divide(6,-3), -2)
    #     self.assertEqual(divide(-6,-3), 2)
        
if __name__ == '__main__':
    unittest.main()
    
# print(calc.add(10, 5))  # should be 15
# print(calc.subtract(10, 5))  # should be 5
# print(calc.multiply(10, 5))  # should be 50
# print(calc.divide(10, 5))  # should be 2