import unittest
from find_product import find_product, find_product_optimized


class Test(unittest.TestCase):
    def test_find_product(self):
        self.assertEqual(find_product([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(find_product([4, 2, 1, 5, 0]), [0, 0, 0, 0, 40])
        
        self.assertEqual(find_product_optimized([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(find_product_optimized([4, 2, 1, 5, 0]), [0, 0, 0, 0, 40])
        
        
if __name__ == '__main__':
    unittest.main()