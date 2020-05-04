import unittest
from a_circle_two_squares import find_area_of_inner_square

class Test(unittest.TestCase):
    def test_find_area_of_inner_square(self):
        self.assertEqual(find_area_of_inner_square(5), 50)
        self.assertEqual(find_area_of_inner_square(6), 72)
        self.assertEqual(find_area_of_inner_square(7), 98)
        
if __name__ == '__main__':
    unittest.main()