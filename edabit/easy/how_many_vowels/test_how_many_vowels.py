import unittest
from how_many_vowels import count_vowels

class Test(unittest.TestCase):
    
    def test_how_many_vowels(self):
        self.assertEqual(count_vowels('Celebration'), 5)
        self.assertEqual(count_vowels('Palm'), 1)
        self.assertEqual(count_vowels('Prediction'), 4)
        
if __name__ == '__main__':
    unittest.main()