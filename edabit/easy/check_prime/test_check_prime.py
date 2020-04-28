import unittest
from check_prime import check_prime

class Test(unittest.TestCase):
    def test_check_prime(self):
        self.assertEqual(check_prime(1), False)
        self.assertEqual(check_prime(31), True)
        self.assertEqual(check_prime(-31), False)
        self.assertEqual(check_prime(-3.1), False)
        self.assertEqual(check_prime(3.1), False)
        self.assertEqual(check_prime(18), False)
        self.assertEqual(check_prime(11), True)
        
if __name__ == "__main__":
    unittest.main()
        