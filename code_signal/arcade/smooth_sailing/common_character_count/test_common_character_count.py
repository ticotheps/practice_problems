import unittest
from common_character_count import commonCharacterCount

class Test(unittest.TestCase):
    def test_commonCharacterCount(self):
        self.assertEquals(commonCharacterCount("aabcc", "adcaa"), 3)
        self.assertEquals(commonCharacterCount("zzzz", "zzzzzzz"), 4)
        
if __name__ == "__main__":
    unittest.main()