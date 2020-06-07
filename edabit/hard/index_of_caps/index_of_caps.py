"""
RETURN THE INDEX OF ALL CAPITAL LETTERS

Create a function that takes in a single string as an argument and returns an
ordered list containing the indices of all capital letters in the string.

Examples:
    - index_of_caps("eDaBiT") ➞ [1, 3, 5]
    - index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
    - index_of_caps("determine") ➞ []
    - index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
    - index_of_caps("sUn") ➞ [1]
    
Notes:
    - Return an empty list if no uppercase letters are found in the string.
    - Special characters ($#A%) and numbers will be included in some test cases.
"""
"""
PHASE I: UNDERSTAND the problem

- Objective:
    - Write an algorithm that takes in a single input (of string data type) and
      returns a single output (of list data type) containing the indices of any
      uppercase letters from the given input string.
      
- Expected Inputs:
    - Number Of: 1
    - Data Type(s): string
    - Var Name(s): 'str'
    
- Expected Outputs:
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): 'caps_indices'
    
- Constraints:
    - Can the input be an empty string?
        - Yes. In this case, just return an empty list as the output.
    - Can the input include non-alphnumeric characters?
        - Yes.
    - Can the input be a negative number?
        - Yes.
    - Can the input be a floating point number?
        - Yes.

PHASE II: devise a PLAN
PHASE III: EXECUTE the plan
PHASE IV: REFLECT on/REFACTOR the solution
"""