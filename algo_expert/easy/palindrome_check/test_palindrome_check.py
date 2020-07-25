import unittest
from palindrome_check import isPalindrome

class Test(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertEqual(isPalindrome("abcdcba"), True)
        self.assertEqual(isPalindrome("a"), True)
        self.assertEqual(isPalindrome("ab"), False)
        self.assertEqual(isPalindrome("aba"), True)
        self.assertEqual(isPalindrome("abb"), False)
        self.assertEqual(isPalindrome("abba"), True)
        self.assertEqual(isPalindrome("abcdefghhgfedcba"), True)
        self.assertEqual(isPalindrome("abcdefghihgfedcba"), True)
        self.assertEqual(isPalindrome("abcdefghihgfeddcba"), False)
        
if __name__ == "__main__":
    unittest.main()