import unittest
from second_lowest_performers import find_second_lowest_performers


class Test(unittest.TestCase):
    def test_find_second_lowest_performers(self):
        self.assertEqual(find_second_lowest_performers([
            ["Harry", 37.21],
            ["Berry", 37.21],
            ["Tina", 37.2],
            ["Akriti", 41],
            ["Harsh", 39]
        ]), ["Berry", "Harry"])
        
        
if __name__ == '__main__':
    unittest.main()