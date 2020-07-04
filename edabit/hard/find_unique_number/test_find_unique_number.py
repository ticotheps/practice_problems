import unittest
from find_unique_number import find_unique_num

class Test(unittest.TestCase):
    def test_find_unique_num(self):
        self.assertEqual(find_unique_num([3, 3, 3, 7, 3, 3]), 7)
        self.assertEqual(find_unique_num([0, 0, 0.77, 0, 0]), 0.77)
        self.assertEqual(find_unique_num([0, 1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(find_unique_num([-4, -4, -4, 4]), 4)
        self.assertEqual(find_unique_num([8, 8, 8, 8, 8, 8, 8, 0.5]), 0.5)
        self.assertEqual(find_unique_num([2, 1, 2, 2, 2, 2, 2, 2]), 1)
        
if __name__ == '__main__':
    unittest.main()