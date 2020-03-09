import unittest
from even_number_generator import find_even_nums

class Test(unittest.TestCase):
    
    def test_even_number_generator(self):
        self.assertEqual(find_even_sum(8), [2, 4, 6, 8])
        self.assertEqual(find_even_sum(4), [2, 4])
        self.assertEqual(find_even_sum(2), [2])
        
if __name__ == '__main__':
    unittest.main()