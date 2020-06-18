import unittest
from triangular_number_sequence import triangle

class Test(unittest.TestCase):
    def test_triangle(self):
        self.assertEqual(triangle(1), 1)
        self.assertEqual(triangle(6), 21)
        self.assertEqual(triangle(215), 23220)
        
if __name__ == '__main__':
    unittest.main()