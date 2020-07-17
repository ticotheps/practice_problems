import unittest
from grade_percentage import grade_percentage

class Test(unittest.TestCase):
    def test_grade_percentage(self):
        self.assertEqual(grade_percentage("85%", "85%"), "You PASSED the Exam")
        self.assertEqual(grade_percentage("99%", "85%"), "You PASSED the Exam")
        self.assertEqual(grade_percentage("65%", "90%"), "You FAILED the Exam")
        self.assertEqual(grade_percentage("65%", "66%"), "You FAILED the Exam")
        
if __name__ == "__main__":
    unittest.main()