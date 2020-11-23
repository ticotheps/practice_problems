import unittest
from sum2 import sum2

class Test(unittest.TestCase):
    def test_sum2(self):
        self.assertEqual(sum2("5125515215521515", "125261616261626"), "5250776831783141")
        
if __name__ == '__main__':
    unittest.main()