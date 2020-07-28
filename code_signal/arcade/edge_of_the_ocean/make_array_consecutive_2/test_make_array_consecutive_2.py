import unittest
from make_array_consecutive_2 import makeArrayConsecutive2

class Test(unittest.TestCase):
    def test_makeArrayConsecutive2(self):
        self.assertEqual(makeArrayConsecutive2([6, 2, 3, 8]), 3)
        self.assertEqual(makeArrayConsecutive2([0, 3]), 2)
        self.assertEqual(makeArrayConsecutive2([5, 4, 6]), 0)
        self.assertEqual(makeArrayConsecutive2([6, 3]), 2)
        self.assertEqual(makeArrayConsecutive2([1]), 0)
        
if __name__ == "__main__":
    unittest.main()