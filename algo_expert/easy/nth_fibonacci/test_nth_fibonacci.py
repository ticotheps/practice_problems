import unittest
from nth_fibonacci import getNthFib

class Test(unittest.TestCase):
    def test_nth_fibonacci(self):
        self.assertEqual(getNthFib(2), 1)
        self.assertEqual(getNthFib(4), 2)
        self.assertEqual(getNthFib(6), 5)
        self.assertEqual(getNthFib(0), f"Sorry. Please pass an input value greater than 0.")
        
if __name__ == '__main__':
    unittest.main()
        