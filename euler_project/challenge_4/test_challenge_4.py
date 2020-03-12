import unittest
from challenge_4 import check_palindrome
from challenge_4 import find_largest_palindrome_product


class Test(unittest.TestCase):
    def test_check_palindrome(self):
        self.assertEqual(check_palindrome(12), False)
        self.assertEqual(check_palindrome(22), True)
        self.assertEqual(check_palindrome(22022), True)
        
    def test_find_largest_palindrome_product(self):
        self.assertEqual(find_largest_palindrome_product(1), 9)
        self.assertEqual(find_largest_palindrome_product(2), 9009)
        self.assertEqual(find_largest_palindrome_product(3), 90909)
    
if __name__ == '__main__':
    unittest.main()