import unittest
from alphabet_soup import alphabet_soup, alphabet_soup_optimized

class Test(unittest.TestCase):
    def test_alphabet_soup(self):
        self.assertEqual(alphabet_soup('hello'), 'ehllo')
        self.assertEqual(alphabet_soup('edabit'), 'abdeit')
        self.assertEqual(alphabet_soup('hacker'), 'acehkr')
        self.assertEqual(alphabet_soup('geek'), 'eegk')
        self.assertEqual(alphabet_soup('javascript'), 'aacijprstv')
        
    def test_alphabet_soup_optimized(self):
        self.assertEqual(alphabet_soup_optimized('hello'), 'ehllo')
        self.assertEqual(alphabet_soup_optimized('edabit'), 'abdeit')
        self.assertEqual(alphabet_soup_optimized('hacker'), 'acehkr')
        self.assertEqual(alphabet_soup_optimized('geek'), 'eegk')
        self.assertEqual(alphabet_soup_optimized('javascript'), 'aacijprstv')
        
if __name__ == '__main__':
    unittest.main()