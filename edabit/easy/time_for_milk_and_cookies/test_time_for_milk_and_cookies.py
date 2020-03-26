import unittest
import datetime
from time_for_milk_and_cookies import time_for_milk_and_cookies

class Test(unittest.TestCase):
    
    def test_time_for_milk_and_cookies(self):
        self.assertEqual(time_for_milk_and_cookies(datetime.date(2013, 12, 24)), True)
        self.assertEqual(time_for_milk_and_cookies(datetime.date(2013, 1, 23)), False)
        self.assertEqual(time_for_milk_and_cookies(datetime.date(3000, 12, 24)), True)
        
if __name__ == '__main__':
    unittest.main()