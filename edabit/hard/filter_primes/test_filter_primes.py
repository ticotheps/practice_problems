import unittest
from filter_primes import filter_primes

class Test(unittest.TestCase):
    def test_filter_primes(self):
        self.assertEqual(filter_primes([7, 9, 3, 9, 10, 11, 27]), [7, 3, 11])
        self.assertEqual(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]), [10007, 1009])
        self.assertEqual(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]), [1009, 3, 61, 1087, 1091, 1093, 1097])
        self.assertEqual(filter_primes([-7, 9, -3, 9, 10, 11, 27]), [11])
        self.assertEqual(filter_primes([7.2, 9, 3, 9, 10, 11.1, 27]), [3])
        
if __name__ == '__main__':
    unittest.main()
        