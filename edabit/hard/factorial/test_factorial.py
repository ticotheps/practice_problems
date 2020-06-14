import unittest
from factorial import factorial

class Test(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(-2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(factorial(2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(9), 362880)
        
if __name__ == '__main__':
    unittest.main()