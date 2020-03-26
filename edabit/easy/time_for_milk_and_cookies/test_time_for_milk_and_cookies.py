import unittest
import datetime
from time_for_milk_and_cookies import time_for_milk_and_cookies

class Test(unittest.TestCase):
    
    def test_time_for_milk_and_cookies(self):
        self.assertEqual(time_for_milk_and_cookies(datetime.date(2020, 3, 26)), False)
        self.assertEqual(time_for_milk_and_cookies(datetime.date(2019, 12, 25)), True)
        
if __name__ == '__main__':
    unittest.main()