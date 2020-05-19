import unittest
from drunken_python import int_to_str, str_to_int

class Test(unittest.TestCase):
    def test_int_to_str(self):
        self.assertEqual(int_to_str("4"), 4)
        self.assertEqual(int_to_str("-4"), -4)

    def test_str_to_int(self):
        self.assertEqual(str_to_int(4), "4")
        self.assertEqual(str_to_int(-4), "-4")
        
if __name__ == '__main__':
    unittest.main()