import unittest
from next_in_line import next_in_line

class Test(unittest.TestCase):
    def test_next_in_line(self):
        self.assertEqual(next_in_line([5, 6, 7, 8, 9], 1), [6, 7, 8, 9, 1])
        self.assertEqual(next_in_line([7, 6, 3, 23, 17], 10), [6, 3, 23, 17, 10])
        self.assertEqual(next_in_line([1, 10, 20, 42 ], 6), [10, 20, 42, 6])
        self.assertEqual(next_in_line([], 6), "No list has been selected")
        
if __name__ == '__main__':
    unittest.main()