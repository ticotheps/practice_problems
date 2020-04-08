import unittest
from binary_search import binarySearch

class Test(unittest.TestCase):
    def test_binarySearch(self):
        self.assertEqual(binarySearch([1, 3, 5, 7, 9, 11], 3), 1)
        self.assertEqual(binarySearch([1, 3, 5, 7, 9, 11], 4), -1)
        self.assertEqual(binarySearch([1, 3, 5, 7, 9, 11], 7), 3)
        self.assertEqual(binarySearch([-5, -3, 1, 3, 5, 7], 7), 5)
        self.assertEqual(binarySearch([-5, -3, 1, 3, 5, 7], -5), 0)
        self.assertEqual(binarySearch([-5, -3, 1, 3, 5, 7], 9), -1)
        
if __name__ == '__main__':
    unittest.main()