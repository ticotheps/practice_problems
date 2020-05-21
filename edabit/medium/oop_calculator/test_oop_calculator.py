import unittest
from oop_calculator import add, subtract, multiply, divide

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-1,-2), -3)

    def test_subtract(self):
        self.assertEqual(subtract(2,1), 1)
        self.assertEqual(subtract(2,-1), 3)
        self.assertEqual(subtract(-2,1), -3)

    def test_multiply(self):
        self.assertEqual(multiply(2,3), 6)
        self.assertEqual(multiply(2,-3), -6)
        self.assertEqual(multiply(=2,-3), 6)

    def test_divide(self):
        self.assertEqual(divide(6,3), 2)
        self.assertEqual(divide(6,-3), -2)
        self.assertEqual(divide(-6,-3), 2)
        
if __name__ == '__main__':
    unittest.main()