import unittest
from add_two_string_numbers import add_str_nums

class Test(unittest.TestCase):
    def test_add_str_nums(self):
        self.assertEqual(add_str_nums("4", "5"), "9")
        self.assertEqual(add_str_nums("abcdefg", "3"), "-1")
        self.assertEqual(add_str_nums("1", ""), "1")
        self.assertEqual(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"), 1874682736267235927391936562808774986)

if __name__ == '__main__':
    unittest.main()