import unittest
from is_lucky import isLucky


class Test(unittest.TestCase):
    def test_isLucky(self):
        self.assertEquals(isLucky(1230), True)
        self.assertEquals(isLucky(239017), False)
        self.assertEquals(isLucky(134008), True)
        self.assertEquals(isLucky(10), False)
        self.assertEquals(isLucky(11), True)
        self.assertEquals(isLucky(1010), True)
        self.assertEquals(isLucky(261534), False)
        self.assertEquals(isLucky(100000), False)
        self.assertEquals(isLucky(999999), True)
        self.assertEquals(isLucky(123321), True)
        
if __name__ == "__main__":
    unittest.main()