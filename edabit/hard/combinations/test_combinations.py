import unittest
from combinations import get_combinations

class Test(unittest.TestCase):
    def test_get_combinations(self):
        self.assertEqual(get_combinations(2, 3), 6)
        self.assertEqual(get_combinations(3, 7, 4), 84)
        self.assertEqual(get_combinations(2, 3, 4, 5), 120)
        
if __name__ == '__main__':
    unittest.main()