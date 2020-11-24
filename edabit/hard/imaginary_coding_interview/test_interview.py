import unittest
from imaginary_coding_interview import interview


class Test(unittest.TestCase):
    def test_interview(self):
        self.assertEqual(interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")
        
        
if __name__ == '__main__':
    unittest.main()