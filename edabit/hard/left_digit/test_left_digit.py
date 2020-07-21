import unittest
from left_digit import left_digit

class Test(unittest.TestCase):
    def test_left_digit(self):
        self.assertEqual()(left_digit("TrAdE2W1n95!"), 2)
        self.assertEqual()(left_digit("V3r1ta$"), 3)
        self.assertEqual()(left_digit("U//DertHe1nflu3nC3"), 1)
        self.assertEqual()(left_digit("J@v@5cR1PT"), 5)
        self.assertEqual()(left_digit("0nSlaUgh7*d3atH"), 0)
        self.assertEqual()(left_digit("F8andD3st1nY"), 8)
        
if __name__ == "__main__":
    unittest.main()