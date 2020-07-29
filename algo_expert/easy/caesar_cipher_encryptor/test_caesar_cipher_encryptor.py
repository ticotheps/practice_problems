import unittest
from caesar_cipher_encryptor import caesarCipherEncryptor

class Test(unittest.TestCase):
    def test_caesarCipherEncryptor(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")
        self.assertEqual(caesarCipherEncryptor("abc", 0), "abc")
        self.assertEqual(caesarCipherEncryptor("abc", 3), "def")
        self.assertEqual(caesarCipherEncryptor("xyz", 5), "cde")
        self.assertEqual(caesarCipherEncryptor("abc", 26), "abc")
        self.assertEqual(caesarCipherEncryptor("abc", 52), "abc")
        self.assertEqual(caesarCipherEncryptor("abc", 57), "fgh")
        self.assertEqual(caesarCipherEncryptor("xyz", 25), "wxy")
        self.assertEqual(caesarCipherEncryptor("iwufqnkqkqoolxzzlzihqfm", 25), "hvtepmjpjpnnkwyykyhgpel")
        self.assertEqual(caesarCipherEncryptor("ovmqkwtujqmfkao", 52), "ovmqkwtujqmfkao")
        self.assertEqual(caesarCipherEncryptor("mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf", 7), "tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm")
        self.assertEqual(caesarCipherEncryptor("kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh", 15), "zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw")
        
if __name__ == "__main__":
    unittest.main()