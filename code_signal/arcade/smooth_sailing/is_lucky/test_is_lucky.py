import unittest
from is_lucky import isLucky


class Test(unittest.TestCase):
    def test_isLucky(self):
        self.assertEquals(isLucky(1230), True)
    
if __name__ == "__main__":
    unittest.main()