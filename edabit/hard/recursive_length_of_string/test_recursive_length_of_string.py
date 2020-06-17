import unittest
from recursive_length_of_string import length

class Test(unittest.TestCase):
    def test_length(self):
        self.assertEqual(length('apple'), 5)
        self.assertEqual(length('make'), 4)
        self.assertEqual(length('a'), 1)
        self.assertEqual(length(''), 0)
        
if __name__ == '__main__':
    unittest.main()