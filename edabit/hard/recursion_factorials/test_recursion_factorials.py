import unittest
from recursion_factorials import find_factorial

class Test(unittest.TestCase):
    def test_find_factorial(self):
        self.assertEqual(find_factorial(5), 120)
        self.assertEqual(find_factorial(3), 6)
        self.assertEqual(find_factorial(1), 1)
        self.assertEqual(find_factorial(0), 1)
        
if __name__ == "__main__":
    unittest.main()