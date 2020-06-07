"""
RETURN THE INDEX OF ALL CAPITAL LETTERS

Create a function that takes in a single input_string as an argument and returns an
ordered list containing the indices of all capital letters in the input_string.

Examples:
    - index_of_caps("eDaBiT") ➞ [1, 3, 5]
    - index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
    - index_of_caps("determine") ➞ []
    - index_of_caps("input_strIKE") ➞ [0, 1, 2, 3, 4, 5]
    - index_of_caps("sUn") ➞ [1]
    
Notes:
    - Return an empty list if no uppercase letters are found in the input_string.
    - Special characters ($#A%) and numbers will be included in some test cases.
"""
"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND the problem

- Objective:
    - Write an algorithm that takes in a single input (of input_string data type) and
      returns a single output (of list data type) containing the indices of any
      uppercase letters from the given input input_string.
      
- Expected Inputs:
    - Number Of: 1
    - Data Type(s): input_string
    - Var Name(s): 'input_str'
    
- Expected Outputs:
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): 'caps_indices_list'
    
- Coninput_straints:
    - Can the input be an empty input_string?
        - Yes. In this case, just return an empty list as the output.
    - Can the input include non-alphnumeric characters?
        - Yes.
    - Can the input be a negative number?
        - Yes.
    - Can the input be a floating point number?
        - Yes.

PHASE II: devise a PLAN

- Brute Force Solution:
    (1) Define a function that takes in a single input input_string, 'input_str', and
    returns a single output list, 'caps_indices_list'.
    
    (2) Declare a local var, 'caps_indices_list', that will be returned as the
    output. Initialize it with an empty list.
    
    (3) Iterate through each character of the given input 'input_str' input_string with a
    'for' loop using the iterator, 'i'.
    
        (4) Declare a var, 'char', and initialize it with the value 'input_str[i]'.
    
        (5) Evaluate the iterated-on character, 'i', for its 'is_capitalized' status.
        
            (a) If 'input_str[i]' is a letter of the alphabet AND it is capitalized, append() 'i' to the 'caps_indices_list'.
            
            (b) If 'i' is NOT a capitalized letter, do nothing.
            
    (6) Return the value of 'caps_indices_list'.
    
PHASE III: EXECUTE the plan (Please see below)

PHASE IV: REFLECT on/REFACTOR the solution
"""

def index_of_caps(input_str):
    caps_indices_list = []
    
    for i in range(0, len(input_str)):
        char = input_str[i]
        
        if char.isalpha() == True and char.isupper() == True:
            caps_indices_list.append(i)
    return caps_indices_list

print(index_of_caps("eDaBiT"))  # -> [1, 3, 5]