import unittest
from simon_says import simon_says

class Test(unittest.TestCase):
    def test_simon_says(self):
        self.assertEqual(simon_says([1, 2], [5, 1]), True)
        self.assertEqual(simon_says([1, 2], [5, 5]), False)
        self.assertEqual(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]), True)
        self.assertEqual(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]), False)
        
if __name__ == '__main__':
    unittest.main()