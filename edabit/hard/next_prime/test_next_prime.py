import unittest
from next_prime import get_next_prime

class Test(unittest.TestCase):
    def test_get_next_prime(self):
        self.assertEqual(get_next_prime(12), 13)
        self.assertEqual(get_next_prime(24), 29)
        self.assertEqual(get_next_prime(11), 11)
        
if __name__ == '__main__':
    unittest.main()
        