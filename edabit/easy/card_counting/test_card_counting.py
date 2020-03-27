import unittest
from card_counting import card_couting

class Test(unittest.TestCase):
    
    def test_card_counting(self):
        self.asserEqual(card_counting(), "expected outcome")
        self.asserEqual(card_counting(), "expected outcome")
        self.asserEqual(card_counting(), "expected outcome")

if __name__ == '__main__':
    unittest.main()