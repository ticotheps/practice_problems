import unittest
from string_length_sorter import sort_by_length

class Test(unittest.TestCase):
    def test_sort_by_length(self):
        self.assertEqual(sort_by_length(["Google", "Apple", "Microsoft"]), ['Apple', 'Google', 'Microsoft'])
        self.assertEqual(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]), ['Raphael', 'Leonardo', 'Donatello', 'Michelangelo'])
        self.assertEqual(sort_by_length(["Turing", "Einstein", "Jung"]), ['Jung', 'Turing', 'Einstein'])

if __name__ == '__main__':
    unittest.main()