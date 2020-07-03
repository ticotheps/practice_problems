import unittest
from unique import unique

class Test(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([3, 3, 3, 7, 3, 3]), 7)
        self.assertEqual(unique([0, 0, 0.77, 0, 0]), 0.77)
        self.assertEqual(unique([0, 1, 1, 1, 1, 1, 1, 1]), 0)
        
if __name__ == '__main__':
    unittest.main()