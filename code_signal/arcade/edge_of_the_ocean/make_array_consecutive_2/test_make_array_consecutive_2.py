import unittest
from make_array_consecutive_2 import makeArrayConsecutive2

class Test(unittest.TestCase):
    def test_makeArrayConsecutive2(self):
        self.assertEqual(makeArrayConsecutive2([6, 2, 3, 8]), 3)
        
if __name__ == "__main__":
    unittest.main()