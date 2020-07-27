import unittest
from shape_area import shapeArea

class Test(unittest.TestCase):
    def test_shapeArea(self):
        self.assertEqual(shapeArea(2), 5)
        self.assertEqual(shapeArea(3), 13)
        self.assertEqual(shapeArea(1), 1)
        self.assertEqual(shapeArea(5), 41)
        self.assertEqual(shapeArea(7000), 97986001)
        self.assertEqual(shapeArea(8000), 127984001)
        self.assertEqual(shapeArea(9999), 199940005)
        self.assertEqual(shapeArea(9998), 199900013)
        self.assertEqual(shapeArea(8999), 161946005)
        self.assertEqual(shapeArea(100), 19801)
 
if __name__ == "__main__":
    unittest.main()