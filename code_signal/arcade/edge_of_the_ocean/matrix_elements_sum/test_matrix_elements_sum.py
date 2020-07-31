import unittest
from matrix_elements_sum import matrixElementsSum

class Test(unittest.TestCase):
    def test_matrixElementsSum(self):
        self.assertEqual(matrixElementsSum(
            [
                [0,1,1,2], 
                [0,5,0,0], 
                [2,0,3,3]
            ]), 9)
        self.assertEqual(matrixElementsSum(
            [
                [1,1,1,0], 
                [0,5,0,1], 
                [2,1,3,10]
            ]), 9)
        self.assertEqual(matrixElementsSum(
            [
                [1,1,1],
                [2,2,2], 
                [3,3,3]
            ]), 18)
        self.assertEqual(matrixElementsSum([[0]]), 0)
        self.assertEqual(matrixElementsSum(
            [
                [1,0,3], 
                [0,2,1], 
                [1,2,0]
            ]), 5)
        self.assertEqual(matrixElementsSum([[1],[5],[0],[2]]), 6)
        self.assertEqual(matrixElementsSum([[1,2,3,4,5]]), 15)
        self.assertEqual(matrixElementsSum([[2],[5],[10]]), 17)
        self.assertEqual(matrixElementsSum([[4,0,1],[10,7,0],[0,0,0],[9,1,2]]), 15)
        self.assertEqual(matrixElementsSum([[1]]), 1)
        
        
if __name__ == "__main__":
    unittest.main()