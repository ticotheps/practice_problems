"""
'Get Student Names'

- Objective: Create a function that takes in a dictionary of students and returns a list of
student names in alphabetical order.

- Expected Inputs & Outputs:
    - Inputs: 
        - Number: 1 input
        - Data Type: dictionary
    - Outputs:
        - Number: 1 output
        - Data Type: list
        
- Constraints:
    - Returned list must be in alphabetical order.

- Examples:
    - Input: get_student_names({
        "Student 1" : "Steve",
        "Student 2" : "Becky",
        "Student 3" : "John"
    }) -> ["Becky", "John", "Steve"]
"""

my_dict = {
    "Student 1" : "Tico",
    "Student 2" : "Kayle",
    "Student 3" : "Lucy"
}

# Takes in a dict of students' names and returns an alphabetized list of names
def get_student_names(students_dict):
    # new list to return with alphabetized students
    names_a_to_z_list = []
    
    # displays a list of students' names from 'students_dict'
    students_list = list(students_dict.values())
    
    # sorts the list of students' names
    sorted_students_list = students_list.sort()
    
    return(students_list)

print(get_student_names(my_dict))