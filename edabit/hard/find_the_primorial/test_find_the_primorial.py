import unittest
from find_the_primorial import get_primorial

class Test(unittest.TestCase):
    def test_get_primorial(self):
        self.assertEqual(get_primorial(1), 2)
        self.assertEqual(get_primorial(2), 6)
        self.assertEqual(get_primorial(8), 9699690)
        
if __name__ == '__main__':
    unittest.main()