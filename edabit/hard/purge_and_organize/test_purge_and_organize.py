import unittest
from purge_and_organize import unique_sort

class Test(unittest.TestCase):
    def test_unique_sort(self):
        self.assertEqual(unique_sort([1, 2, 4, 3]), [1, 2, 3, 4])
        self.assertEqual(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]), [1, 2, 3, 4])
        self.assertEqual(unique_sort([6, 7, 3, 2, 1]), [1, 2, 3, 6, 7])
        self.assertEqual(unique_sort([1, 2.243, 4, 3]), [1, 2.243, 3, 4])
        self.assertEqual(unique_sort([1, 2, 4, -3]), [-3, 1, 2, 4])
        
if __name__ == '__main__':
    unittest.main()