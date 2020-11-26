import unittest
from remove_even import remove_even


class Test(unittest.TestCase):
    def test_remove_even(self):
        self.assertEqual(remove_even([1, 2, 4, 5, 10, 6, 3]), [1, 5, 3])
        
if __name__ == "__main__":
    unittest.main()