import unittest
from all_longest_strings import allLongestStrings

class Test(unittest.TestCase):
    def test_allLongestStrings(self):
        self.assertEqual(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]), ["aba", "vcd", "aba"])
        self.assertEqual(allLongestStrings(["aa"]), ["aa"])
        self.assertEqual(allLongestStrings(["abc", "eeee", "abcd", "dcd"]), ["eeee", "abcd"])
        self.assertEqual(allLongestStrings(
            ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]), 
            ["zzzzzz", "abcdef", "aaaaaa"]
        )
        self.assertEqual(allLongestStrings(["enyky", "benyky", "yely", "varennyky"]), ["varennyky"])
        self.assertEqual(allLongestStrings(["abacaba", "abacab", "abac", "xxxxxx"]), ["abacaba"])   
        self.assertEqual(allLongestStrings(
            ["young", "yooooooung", "hot", "or", "not", "come", "on", "fire", "water", "watermelon"]), 
            ["yooooooung", "watermelon"]
        )
        self.assertEqual(allLongestStrings(["onsfnib", "aokbcwthc", "jrfcw"]), ["aokbcwthc"])
        self.assertEqual(allLongestStrings(["lbgwyqkry"]), ["lbgwyqkry"])
        self.assertEqual(allLongestStrings(["i"]), ["i"])
        
        
if __name__ == "__main__":
    unittest.main()