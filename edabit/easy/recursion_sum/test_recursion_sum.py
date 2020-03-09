import unittest
from recursion_sum import sum_numbers

class Test(unittest.TestCase):
    
    def test_recursion_sum(self):
        self.assertEqual(sum_numbers(5), 15)
        self.assertEqual(sum_numbers(1), 1)
        self.assertEqual(sum_numbers(12), 78)
        
if __name__ == '__main__':
    unittest.main()