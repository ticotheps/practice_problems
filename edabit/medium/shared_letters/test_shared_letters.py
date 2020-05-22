import unittest

class Test(unittest.TestCase):
    def test_get_shared_letters(self):
        self.assertEqual(get_shared_letters('apple', 'meaty'), 2)
        self.assertEqual(get_shared_letters('fan', 'forsook'), 1)
        self.assertEqual(get_shared_letters('spout', 'shout'), 4)
        
if __name__ == '__main__':
    unittest.main()