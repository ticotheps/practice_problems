import unittest
from find_three_largest_numbers import findThreeLargestNumbers

class Test(unittest.TestCase):
    def test_findThreeLargestNumbers(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
        
if __name__ == '__main__':
    unittest.main()