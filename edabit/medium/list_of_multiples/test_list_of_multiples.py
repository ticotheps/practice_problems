import unittest
from list_of_multiples import list_of_multiples

class Test(unittest.TestCase):
    def test_list_of_multiples(self):
        self.assertEqual(list_of_multiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(list_of_multiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120])
        self.assertEqual(list_of_multiples(17, 6), [17, 34, 51, 68, 85, 102])
        
if __name__ == '__main__':
    unittest.main()