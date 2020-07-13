import unittest
from remove_smallest import remove_smallest

class Test(unittest.TestCase):
    def test_remove_smallest(self):
        self.assertEqual(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
        self.assertEqual(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
        self.assertEqual(remove_smallest([2, 2, 1, 2, 1]), [2, 2, 2, 1])
        self.assertEqual(remove_smallest([3, 1, 6, 7, 3, 7, 6]), [3, 6, 7, 3, 7, 6])
        self.assertEqual(remove_smallest([4, 4, 4, 1]), [4, 4, 4])
        self.assertEqual(remove_smallest([5, 4, 5, 3, 1, 1]), [5, 4, 5, 3, 1])
        self.assertEqual(remove_smallest([1, 5, 3]), [5, 3])
        self.assertEqual(remove_smallest([]), [])
        self.assertEqual(remove_smallest([6, 2, 5, 4, 8, 6, 3, 2, 7]), [6, 5, 4, 8, 6, 3, 2, 7])
        self.assertEqual(remove_smallest([3]), [])

if __name__ == "__main__":
    unittest.main()