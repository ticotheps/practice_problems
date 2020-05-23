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

PHASE II - DEVISING A PLAN

PHASE III - EXECUTING THE PLAN

PHASE IV - REFLECTING ON/REFACTORING THE PLAN
"""