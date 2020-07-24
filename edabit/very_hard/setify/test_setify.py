import unittest
from setify import setify

class Test(unittest.TestCase):
    def test_setify(self):
        self.assertEqual(setify([1, 3, 3, 5, 5]), [1, 3, 5])
        self.assertEqual(setify([4, 4, 4, 4]), [4])
        self.assertEqual(setify([5, 7, 8, 9, 10, 15]), [5, 7, 8, 9, 10, 15])
        self.assertEqual(setify([5, 9, 9]), [5, 9])
        self.assertEqual(setify([1, 2, 3, 4, 5, 5, 6, 6, 7]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(setify([1, 1, 2, 2, 2]), [1, 2])
        
if __name__ == "__main__":
    unittest.main()