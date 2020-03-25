import unittest
from get_student_names import get_student_names

class Test(unittest.TestCase):
    
    def test_get_student_names(self):
        self.assertEqual(get_student_names({
        "Student 1" : "Steve",
        "Student 2" : "Becky",
        "Student 3" : "John"
    }), ["Becky", "John", "Steve"])
        
        
if __name__ == '__main__':
    unittest.main()