import unittest
from find_three_largest_numbers import find_three_largest_numbers

class Test(unittest.Testcase):
    def test_find_three_largest_numbers(self):
        self.assertEqual(find_three_largest_numbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
        
if __name__ == '__main__':
    unittest.main()