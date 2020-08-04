import unittest
from all_longest_strings import allLongestStrings

class Test(unittest.TestCase):
    def test_allLongestStrings(self):
        self.assertEqual(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]), ["aba", "vcd", "aba"])
        
        
if __name__ == "__main__":
    unittest.main()