import unittest
from card_counting import count

class Test(unittest.TestCase):
    
    def test_count(self):
        self.assertEqual(count(), "expected outcome")
        self.assertEqual(count(), "expected outcome")
        self.assertEqual(count(), "expected outcome")

if __name__ == '__main__':
    unittest.main()