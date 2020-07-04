import unittest
from unique import find_unique_num

class Test(unittest.TestCase):
    def test_find_unique_num(self):
        self.assertEqual(find_unique_num([3, 3, 3, 7, 3, 3]), 7)
        self.assertEqual(find_unique_num([0, 0, 0.77, 0, 0]), 0.77)
        self.assertEqual(find_unique_num([0, 1, 1, 1, 1, 1, 1, 1]), 0)
        
if __name__ == '__main__':
    unittest.main()