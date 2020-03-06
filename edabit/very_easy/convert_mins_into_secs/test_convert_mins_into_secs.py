import unittest
from convert_mins_into_secs import convert

class Test(unittest.TestCase):
    
    def test_convert_mins_into_secs(self):
        self.assertEqual(convert(5), "300 secs")
        self.assertEqual(convert(2), "120 secs")
        self.assertEqual(convert(10), "600 secs")
        
if __name__ == '__main__':
    unittest.main()
        