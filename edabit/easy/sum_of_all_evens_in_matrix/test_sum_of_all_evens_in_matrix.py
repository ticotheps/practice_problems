import unittest
from sum_of_all_evens_in_matrix import sum_of_evens

class Test(unittest.TestCase):
    def test_sum_of_evens(self):
        self.assertEqual(sum_of_evens([
                            [1, 0, 2],
                            [5, 5, 7],
                            [9, 4, 3]
                        ]), 6)
        self.assertEqual(sum_of_evens([
                            [1, 1],
                            [1, 1]
                        ]), 0)
        self.assertEqual(sum_of_evens([
                            [42, 9],
                            [16, 8]
                        ]), 66)
        self.assertEqual(sum_of_evens([
                            [],
                            [],
                            []
                        ]), 0)
        
if __name__ == '__main__':
    unittest.main()