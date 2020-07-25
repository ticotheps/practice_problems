import unittest
from missing_num import missing_num

class Test(unittest.TestCase):
    def test_missing_num(self):
        self.assertEqual(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]), 5)
        self.assertEqual(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]), 10)
        self.assertEqual(missing_num([7, 2, 3, 9, 4, 5, 6, 8, 10]), 1)
        self.assertEqual(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]), 7)
        self.assertEqual(missing_num([1, 7, 2, 4, 8, 10, 5, 6, 9]), 3)
        
if __name__ == "__main__":
    unittest.main()