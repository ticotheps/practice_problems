import unittest
from filter_out_strings import filter_out_strings

class Test(unittest.TestCase):
    def test_filter_out_strings(self):
        self.assertEqual(filter_out_strings([]), """Invalid input. Please try a list with at least one element.""")
        self.assertEqual(filter_out_strings([1, 2, "a", "b"]), [1, 2])
        self.assertEqual(filter_out_strings([1, "a", "b", 0, 15]), [1, 0, 15])
        self.assertEqual(filter_out_strings([1, 2, "aasf", "1", "123", 123]), [1, 2, 123])
        
if __name__ == '__main__':
    unittest.main()