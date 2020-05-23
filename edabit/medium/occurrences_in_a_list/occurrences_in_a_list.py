"""
ALL OCCURRENCES OF AN ELEMENT IN A LIST

Objective:
    - Create a function that returns the indices of all occurrences of an item in the
list.

Examples:
    - get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]
    - get_indices([1, 5, 5, 2, 7], 7) ➞ [4]
    - get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]
    - get_indices([1, 5, 5, 2, 7], 8) ➞ []
    
Notes:
    - If an element does not exist in a list, return [].
    - Lists are zero-indexed.
    - Values in the list will be value-types (don't need to worry about nested lists).
"""
"""
PHASE I - UNDERSTANDING THE PROBLEM
    - Objective:
        - Write an algorithm that will take in two inputs, (1) a list and (2) a
        string or integer that may or may not occurr in the given list, and then
        returns a single list of the indices in which the second input occurs.
        
    - Expected Inputs:
        - Number: 2
        - Data Types: list, string/integer
        - Var Names: 'input_list', 'input_element'
        
    - Expected Outputs:
        - Number: 1
        - Data Types: list
        - Var Name: 'indices_list'
        
    - Constraints:
        - Can the elements be negative numbers?
            - Yes.
        - Can the elements be empty strings?
            - No.
            - Must be alpha-numeric characters.
        - Can the elements be floating point numbers?
            - No.
            - Must be whole integers

PHASE II - DEVISING A PLAN
    - First-Pass Solution:
        (1) Define a function that takes in 2 params and returns 1 output.
        
        (2) Declare a var to represent the output. Initialize it with '[]'.
        
        (3) Use a 'for' loop to iterate over an enumerated version of the
        'input_list'.
        
            (4) Evaluate for any items in the 'input_list' that are identical matches
            with the 'input_element'.
            
            (5) If an iterated-on element matches the 'input_element', append the associated enumerated value to the var declared in step 2.
        
        (6) Return the var declared in step 2.

PHASE III - EXECUTING THE PLAN (PLEASE SEE BELOW)

PHASE IV - REFLECTING ON/REFACTORING THE PLAN
    - Asymptotic Analysis:
        - First-Pass Solution:
            - Time Complexity:
                - O(n) -> 'linear'
            - Space Complexity:
                - O(1) -> 'constant'
"""

def get_indices(input_list, input_element):
    indices_list = []
    for index, item in enumerate(input_list):
        if item == input_element:
            indices_list.append(index)    
    return indices_list