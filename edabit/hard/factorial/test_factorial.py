import unittest
from factorial import factorial, optimized_factorial

class Test(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(-2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(factorial(2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(12), 479001600)
        
    def test_optimized_factorial(self):
        self.assertEqual(optimized_factorial(-2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(optimized_factorial(2.133), "Invalid input. Please try a positive integer instead.")
        self.assertEqual(optimized_factorial(4), 24)
        self.assertEqual(optimized_factorial(0), 1)
        self.assertEqual(optimized_factorial(9), 362880)
        self.assertEqual(optimized_factorial(12), 479001600)
        
if __name__ == '__main__':
    unittest.main()