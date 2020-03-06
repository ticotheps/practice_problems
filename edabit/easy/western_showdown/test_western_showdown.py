import unittest
from western_showdown import showdown

class Test(unittest.TestCase):
    
    def test_western_showdown(self):
        self.assertEqual(showdown("dude ", "dude"), "Err: Please pass in 2 arguments of equal lengths and try again")
        self.assertEqual(showdown("dude", "dude"), "tie")
        self.assertEqual(showdown(" dude ", "dude  "), "p2")
        self.assertEqual(showdown("dude  ", "  dude"), "p1")
        
if __name__ == '__main__':
    unittest.main()