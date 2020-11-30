import unittest
from find_product import find_product


class Test(unittest.TestCase):
    def test_find_product(self):
        self.assertEqual(find_product([1, 2, 3, 4]), [24, 12, 8, 6])
        
        
if __name__ == '__main__':
    unittest.main()