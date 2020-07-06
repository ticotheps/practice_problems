import unittest
from nth_smallest_element import nth_smallest

class Test(unittest.TestCase):
    def test_nth_smallest(self):
        self.assertEqual(nth_smallest([1, 3, 5, 7], 1), 1)
        self.assertEqual(nth_smallest([1, 3, 5, 7], 3), 5)
        self.assertEqual(nth_smallest([1, 3, 5, 7], 5), None)
        self.assertEqual(nth_smallest([7, 3, 5, 1], 2), 3)
        self.assertEqual(nth_smallest([5, 4, 3, 2, 1, -3], 1), -3)
        self.assertEqual(nth_smallest([5, 4, 3, 2, 1, -3], 5), 4)
        self.assertEqual(nth_smallest([4, 5], 3), None)
        self.assertEqual(nth_smallest([4, 5], 2), 5)
        self.assertEqual(nth_smallest([4, 5], 1), 4)
        
if __name__ == "__main__":
    unittest.main()