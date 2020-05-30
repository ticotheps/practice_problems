import unittest
from first_repeating_character import first_repeat

class Test(unittest.TestCase):
    def test_first_repeat(self):
        self.assertEqual(first_repeat('legolas'), 'l')
        self.assertEqual(first_repeat('Gandalf'), 'a')
        self.assertEqual(first_repeat('Balrog'), -1)
        self.assertEqual(first_repeat('Isildur'), -1)
        
if __name__ == '__main__':
    unittest.main()