import unittest
from fizzbuzz_interview_question import fizz_buzz

class Test(unittest.TestCase):
    def test_fizzbuzz_interview_question(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(4), "4")
        
if __name__ == '__main__':
    unittest.main()