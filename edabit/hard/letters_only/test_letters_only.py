import unittest
from letters_only import letters_only

class Test(unittest.TestCase):
    def test_letters_only(self):
        self.assertEqual(letters_only("R!=:~0o0./c&}9k`60=y"), "Rocky")
        self.assertEqual(letters_only("^,]%4B|@56a![0{2m>b1&4i4"), "Bambi")
        self.assertEqual(letters_only("^U)6$22>8p)."), "Up")

if __name__ == "__main__":
    unittest.main()