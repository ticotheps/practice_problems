"""
LETTERS SHARED BETWEEN TWO WORDS

Create a function that returns the number of characters shared between two
words.

Examples:
    - get_shared_letters('apple', 'meaty') -> 2
    - get_shared_letters('fan', 'forsook') -> 1
    - get_shared_letters('spout', 'shout') -> 4
"""

"""
PHASE I - UNDERSTAND THE PROBLEM

Objective:
    - Create an algorithm that takes in two inputs, 'str_1' and 'str_2', and
    returns a single output, 'num_of_shared_letters'.
    
Expected Inputs & Outputs:
    - Inputs:
        - Expected Number: 2
        - Expected Data Types: string, string
        - Expected Var Names: 'str_1', 'str_2'

    - Outputs:
        - Expected Number: 1
        - Expected Data Types: integer
        - Expected Var Names: 'num_of_shared_letters'
        
Constraints:
    - Can either of the inputs be empty strings?
        - No.
    - Can the strings include non-alphanumeric characters?
        - No. They must be letters.
"""

# PHASE II - DEVISE A PLAN
# PHASE III - EXECUTE THE PLAN

# Create a function that takes in two string inputs
def get_shared_letters(str_1, str_2):
    # Declare a var that will represent the output and initialize it with 0
    num_of_shared_letters = 0
    
    # Declare a dictionary that will store key:value pairs where the keys are
    #   distinct letters from str_1 and the values are the numbers of 
    #   occurrences of that letter in str_1.
    str_1_dict = {}
    
    # Use a 'for' loop to iterate through the first input string
    for letter in str_1:
        
        # Check to see if each letter from str_1 exists in str_1_dict
        if letter in str_1_dict:
            str_1_dict[letter] += 1

        # If it doesn't already exist, add the letter as a new entry
        else:
            str_1_dict[letter] = 1
     
    # Use a 'for' loop to iterate through the second input string       
    for letter in str_2:
        # Check to see if each letter from str_2 exists in str_1_dict
        # # If it does exist, add 1 to the value of 'num_of_shared_letters'
        if letter in str_1_dict:
            num_of_shared_letters += 1
    
    return num_of_shared_letters

"""
PHASE IV - REFLECT/REFACTOR

Asymptotic Analysis:
    - Time Complexity:
        - O(n) -> 'linear'
    - Space Complexity:
        - O(n) -> 'linear'
"""