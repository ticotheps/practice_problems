import unittest
from drunken_python import int_to_str, str_to_int

class Test(unittest.TestCase):
    def test_int_to_str(self):
        self.assertEqual(int_to_str(4), '4')
        self.assertEqual(int_to_str(-4), '-4')
        self.assertEqual(int_to_str(0.4), """Please enter a whole number for the 'num_int' input instead of a floating point number""")

    def test_str_to_int(self):
        self.assertEqual(str_to_int('4'), 4)
        self.assertEqual(str_to_int('-4'), -4)
        self.assertEqual(str_to_int('0.4'), """Please enter a string with a whole number value for the 'num_str' input instead of a string with a floating point number value inside of it""")
        
if __name__ == '__main__':
    unittest.main()