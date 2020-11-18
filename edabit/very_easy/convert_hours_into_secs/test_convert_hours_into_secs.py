import unittest
from convert_hours_into_secs import how_many_seconds

class Test(unittest.TestCase):
    def test_how_many_seconds(self):
        self.assertEqual(how_many_seconds(1), 3600)
        self.assertEqual(how_many_seconds(2), 7200)
        self.assertEqual(how_many_seconds(5), 18000)
        self.assertEqual(how_many_seconds(10), 36000)
        self.assertEqual(how_many_seconds(12), 43200)
        self.assertEqual(how_many_seconds(24), 86400)
        self.assertEqual(how_many_seconds(2.5), 9000)
    def test_none_value_for_input(self):
        self.assertRaises(TypeError, how_many_seconds)
    def test_negative_value_for_input(self):
        self.assertRaises(TypeError, how_many_seconds)

        
if __name__ == '__main__':
    unittest.main()