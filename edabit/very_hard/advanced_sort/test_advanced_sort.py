import unittest
from advanced_sort import advanced_sort

class Test(unittest.TestCase):
    def test_advanced_sort(self):
        self.assertEqual(advanced_sort([1,2,1,2]) , [[1,1],[2,2]])
        self.assertEqual(advanced_sort([2,1,2,1]) , [[2,2],[1,1]])
        self.assertEqual(advanced_sort([3,2,1,3,2,1]) , [[3,3],[2,2],[1,1]])
        self.assertEqual(advanced_sort([5,5,4,3,4,4]) , [[5,5],[4,4,4],[3]])
        self.assertEqual(advanced_sort([80,80,4,60,60,3]),[[80,80],[4],[60,60],[3]])
        self.assertEqual(advanced_sort(['c','c','b','c','b',1,1]),[['c','c','c'],['b','b'],[1,1]])
        self.assertEqual(advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]),[[1234, 1234],[1235, 1235, 1235],[1236]])
        self.assertEqual(advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']),[['1234', '1234'],['1235', '1235', '1235'],['1236']])
        
if __name__ == "__main__":
    unittest.main()