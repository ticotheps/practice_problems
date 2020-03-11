"""
List of Multiples
    - Objective: Create a function that takes two numbers as arguments (num, length) and returns
    a list of multiples of num up to length.
    
    - Examples:
        - get_list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
        - get_list_of_multiples(12, 10) -> [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
        - get_list_of_multiples(17, 6) -> [17, 34, 51, 68, 85, 102]
        
    - Hints:
        - Note that our argument 'num' is also included in the returned list.
"""
"""
UNDERSTANDING THE PROBLEM:
    - Objective: Create an algorithm that takes in 2 inputs ("num", "length")
    and returns 1 output, "multiples_list", containing "length" number of
    multiples in the list (one of which includes the "num" itself).
    
    - Expected Inputs/Outputs:
        - Inputs: 2
            - "num" (data type: integer)
            - "length" (data type: integer)
        - Outputs: 1
            - "multiples_list" (data type: python list)
            
    - Constraints:
        - "num" must be an positive, whole integer.
        - "length" must be an positive, whole integer.
        - "num" & "length" cannot be negative numbers.
        - "num" & "length" cannot be floating point numbers.
        
    - Hints:
        - Note that the "num" argument will always be the first item in the returned list.
"""
"""
DEVISING A PLAN:

"""
def get_list_of_multiples (num, length):
    return num

print(get_list_of_multiples(7, 5))
print(get_list_of_multiples(12, 10))
print(get_list_of_multiples(17, 6))