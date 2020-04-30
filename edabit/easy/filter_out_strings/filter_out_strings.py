"""
FILTER OUT STRINGS FROM AN ARRAY

Objective: 
    - Create a function that takes in a list of non-negative integers and
        strings and returns a new list without the strings.
        
Examples:
    - filter_out_strings([1, 2, "a", "b"]) -> [1, 2]
    - filter_out_strings([1, "a", "b", 0, 15]) -> [1, 0, 15]
    - filter_out_strings([1, 2, "aasf", "1", "123", 123]) -> [1, 2, 123]
    
Notes:
    - Zero is a non-negative integer.
"""

"""
UNDERSTAND PHASE

Defining Terms:
    - "non-negative integers": positive whole numbers

Expected Inputs & Outputs:
    - Inputs:
        - Expected Number: 1
        - Expected Data Type: list
        - Expected Variable Name: 'input_list'
        
    - Outputs:
        - Expected Number: 1
        - Expected Data Type: list
        - Expected Variable Name: 'filtered_list'

Constraints:
    - Can the 'input_list' variable be an empty list?
        - Yes. If this is the case, return a string that says, "Please enter a
            valid input and try again".
    - Can the elements of the 'input_list' variable be floating point numbers?
        - No.
    - Can the elements of the 'input_list' variable be negative numbers?
        - No.
"""

# PLAN PHASE + EXECUTE PHASE

def filter_out_strings(input_list):
    # Initialize a var with an empty list to be returned as the output
    filtered_list = []
    print(f"\nfiltered_list = {filtered_list}")
    
    # Iterate through the 'input_list'
    for element in input_list:
        print(f"element = {element}")
        
        # Create a var that stores the type of each iterated element
        element_type = type(element)
        print(f"element_type of {element} = {element_type}")
        
        # If 'element_type' is NOT of type 'str', append it to the 
        #   'filtered_list'.
        if element_type != str:
            filtered_list.append(element)
    
    return filtered_list

print(filter_out_strings([1, 2, "a", "b"])) # should print [1, 2]
print(filter_out_strings([1, "a", "b", 0, 15])) # should print [1, 0, 15]
print(filter_out_strings([1, 2, "aasf", "1", "123", 123])) # should print [1, 2, 123]

"""
REFLECT/REFACTOR PHASE

"""