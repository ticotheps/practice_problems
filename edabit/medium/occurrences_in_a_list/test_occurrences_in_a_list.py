import unittest
from occurrences_in_a_list import get_indices

class Test(unittest.TestCase):
    def test_get_occurrences(self):
        self.assertEqual(get_indices(['a', 'a', 'b', 'a', 'b', 'a'], 'a'), [0, 1, 3, 5])
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 7), [4])
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 5), [1, 2])
        self.assertEqual(get_indices([1, 5, 5, 2, 7], 8), [])
        
if __name__ == '__main__':
    unittest.main()