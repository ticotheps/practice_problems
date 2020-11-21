import unittest
from amplify_multiples_of_four import amplify

class Test(unittest.TestCase):
    def test_amplify(self):
        self.assertEqual(amplify(4), [1, 2, 3, 40])
        self.assertEqual(amplify(3), [1, 2, 3])
        self.assertEqual(amplify(25), [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25])
        
if __name__ == '__main__':
    unittest.main()