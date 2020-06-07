import unittest
from index_of_caps import index_of_caps

class Test(unittest.TestCase):
    def test_index_of_caps(self):
        self.assertEqual(index_of_caps("eDaBiT"), [1, 3, 5])
        self.assertEqual(index_of_caps("eQuINoX"), [1, 3, 4, 6])
        self.assertEqual(index_of_caps("determine"), [])
        self.assertEqual(index_of_caps("STRIKE"), [0, 1, 2, 3, 4, 5])
        self.assertEqual(index_of_caps("sUn"), [1])
        
if __name__ == '__main__':
    unittest.main()