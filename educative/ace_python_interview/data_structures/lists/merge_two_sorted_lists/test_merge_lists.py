import unittest
from merge_lists import merge_lists


class Test(unittest.TestCase):
    def test_merge_lists(self):
        self.assertEqual(merge_lists([1, 3, 4, 5], [2, 6, 7, 8]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_lists([4, 5, 6], [-2, -1, 0, 7]), [-2, -1, 0, 4, 5, 6, 7])
        
if __name__ == '__main__':
    unittest.main()