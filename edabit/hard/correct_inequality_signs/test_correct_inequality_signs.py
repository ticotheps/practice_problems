import unittest
from correct_inequality_signs import correct_signs

class Test(unittest.TestCase):
    def test_correct_signs(self):
        self.assertEqual(correct_signs(3), 'Invalid input. Please provide an input of string data type.')
        self.assertEqual(correct_signs("3 < 7 <"), 'Invalid input. Please provide an input of string with a valid number of integers and operators in it.')
        self.assertEqual(correct_signs("3 < 7 < 11"), True)
        self.assertEqual(correct_signs("13 > 44 > 33 > 1"), False)
        self.assertEqual(correct_signs("1 < 2 < 6 < 9 > 3"), True)
        
    
if __name__ == "__main__":
    unittest.main()