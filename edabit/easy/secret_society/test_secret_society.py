import unittest
from secret_society import get_society_name

class Test(unittest.TestCase):
    
    def test_get_society_name(self):
        self.assertEqual(get_society_name(['Adam', 'Sarah', 'Malcolm']), 'AMS')
        self.assertEqual(get_society_name(['Harry', 'Newt','Luna', 'Cho']), 'CHLN')
        self.assertEqual(get_society_name(['Phoebe', 'Chandler', 'Rachel', 'Ross', 'Monica', 'Joey']), 'CJMPRR')
        
if __name__ == '__main__':
    unittest.main()