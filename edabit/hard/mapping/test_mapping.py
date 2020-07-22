import unittest
from mapping import mapping

class Test(unittest.TestCase):
    def test_mapping(self):
        self.assertEqual(mapping(["a", "b", "c"]), { "a": "A", "b": "B", "c": "C" })
        self.assertEqual(mapping(["p", "s", "t"]), { "p": "P", "s": "S", "t": "T" })
        self.assertEqual(mapping(["a", "v", "y", "z"]), { "a": "A", "v": "V", "y": "Y", "z": "Z" })
        
if __name__ == "__main__":
    unittest.main()