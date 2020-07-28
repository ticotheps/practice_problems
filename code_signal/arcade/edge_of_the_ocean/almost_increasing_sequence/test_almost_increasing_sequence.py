import unittest
from almost_increasing_sequence import almostIncreasingSequence

class Test(unittest.TestCase):
    def test_almostIncreasingSequence(self):
        self.assertEqual(almostIncreasingSequence([1, 3, 2, 1]), False)
        self.assertEqual(almostIncreasingSequence([1, 3, 2]), True)
        self.assertEqual(almostIncreasingSequence([1, 2, 1, 2]), False)
        self.assertEqual(almostIncreasingSequence([3, 6, 5, 8, 10, 20, 15]), False)
        self.assertEqual(almostIncreasingSequence([1, 1, 2, 3, 4, 4]), False)
        self.assertEqual(almostIncreasingSequence([1, 4, 10, 4, 2]), False)
        self.assertEqual(almostIncreasingSequence([10, 1, 2, 3, 4, 5]), True)
        self.assertEqual(almostIncreasingSequence([1, 1, 1, 2, 3]), False)
        self.assertEqual(almostIncreasingSequence([0, -2, 5, 6]), True)
        self.assertEqual(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]), False)
        self.assertEqual(almostIncreasingSequence([40, 50, 60, 10, 20, 30]), False)
        self.assertEqual(almostIncreasingSequence([1, 1]), True)
        self.assertEqual(almostIncreasingSequence([1, 2, 5, 3, 5]), True)
        self.assertEqual(almostIncreasingSequence([1, 2, 5, 5, 5]), False)
        self.assertEqual(almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1]), False)
        self.assertEqual(almostIncreasingSequence([1, 2, 3, 4, 3, 6]), True)
        self.assertEqual(almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]), True)
        self.assertEqual(almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]), True)
        self.assertEqual(almostIncreasingSequence([3, 5, 67, 98, 3]), True)
        
if __name__ == "__main__":
    unittest.main()