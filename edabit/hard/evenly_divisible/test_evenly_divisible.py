import unittest
from evenly_divisible import evenly_divisible

class Test(unittest.TestCase):
    def test_evenly_divisible(self):
        self.assertEqual(evenly_divisible(1, 10, 2), 30)
        self.assertEqual(evenly_divisible(1, 10, 3), 18)
        self.assertEqual(evenly_divisible(0, 12, 3), 30)
        self.assertEqual(evenly_divisible(-10, -1, 2), -30)
        self.assertEqual(evenly_divisible(-10, -1, 3), -18)
        self.assertEqual(evenly_divisible(1, 10, 20), 0)
        self.assertEqual(evenly_divisible(-10, 10, 2), 0)
        
if __name__ == "__main__":
    unittest.main()