import unittest
from alphanumeric_restriction import alphanumeric_restriction

class Test(unittest.TestCase):
    def test_alphanumeric_restriction(self):
        self.assertEqual(alphanumeric_restriction("Bold"), True)
        self.assertEqual(alphanumeric_restriction("123454321"), True)
        self.assertEqual(alphanumeric_restriction("H3LL0"), False)
        self.assertEqual(alphanumeric_restriction("hhefuhiwfgn"), True)
        self.assertEqual(alphanumeric_restriction("0"), True)
        self.assertEqual(alphanumeric_restriction("hhefuhiwfgn"), True)
        self.assertEqual(alphanumeric_restriction("ed@bit"), False)
        self.assertEqual(alphanumeric_restriction("only letters right"), False)
        self.assertEqual(alphanumeric_restriction("132 143 234"), False)
        self.assertEqual(alphanumeric_restriction("()"), False)
        self.assertEqual(alphanumeric_restriction("Hello"), True)
        self.assertEqual(alphanumeric_restriction("10,000"), False)
        self.assertEqual(alphanumeric_restriction("1a2b3c"), False)
        self.assertEqual(alphanumeric_restriction(""), False)
        
if __name__ == "__main__":
    unittest.main()