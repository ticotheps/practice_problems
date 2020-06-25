import unittest
from alphabet_soup import alphabet_soup

class Test(unittest.TestCase):
    def test_alphabet_soup(self):
        self.assertEqual(alphabet_soup('hello'), 'ehllo')
        self.assertEqual(alphabet_soup('edabit'), 'abdeit')
        self.assertEqual(alphabet_soup('hacker'), 'acehkr')
        self.assertEqual(alphabet_soup('geek'), 'eegk')
        self.assertEqual(alphabet_soup('javascript'), 'aacijprstv')
        
if __name__ == '__main__':
    unittest.main()