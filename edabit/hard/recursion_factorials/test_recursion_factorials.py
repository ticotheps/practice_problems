import unittest
from recursion_factorials import factorial

class Test(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(0), 1)
        
if __name__ == "__main__":
    unittest.main()