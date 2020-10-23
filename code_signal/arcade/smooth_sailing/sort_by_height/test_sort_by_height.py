import unittest
from sort_by_height import sortByHeight


class Test(unittest.TestCase):
    def test_sortByHeight(self):
        self.assertEquals(
            sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]),
            [-1, 150, 160, 170, -1, -1, 180, 190]
        )
        self.assertEquals(
            sortByHeight([-1, -1, -1, -1, -1]),
            [-1, -1, -1, -1, -1]
        )
        self.assertEquals(sortByHeight([-1]),[-1])
        self.assertEquals(
            sortByHeight([4, 2, 9, 11, 2, 16]),
            [2, 2, 4, 9, 11, 16]
        )
        self.assertEquals(
            sortByHeight([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]),
            [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 2]
        )
        self.assertEquals(
            sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]),
            [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77]
        )

if __name__ == "__main__":
    unittest.main()