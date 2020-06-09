"""
CORRECT INEQUALITY SIGNS

Create a function that returns True if a given inequality expression is correct
and False otherwise.
"""

"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND the problem

- Objective:
    - Write an algorithm that takes in a single string (containing a series of
      inequality expressions) as the input and returns a Boolean value as the
      output.
        - If the inequality expression inside of the input string is correct,
          return True.
        - Otherwise, return False.

- Expected Input(s):
    - Number Of: 1
    - Data Type(s): string
    - Var Name(s): 'txt'

- Expected Output(s):
    - Number Of: 1
    - Data Type(s): Boolean
    - Var Name(s): 'is_correct'

- Constraints:
    - Can the given input string include negative numbers?
        - Yes.

    - Can the given input string include floating point numbers?
        - Yes.

    - Can the given input be an empty strings?
        - Yes.

    - If given an empty string, how would you handle that input?
        - Return a string that says, 'Invalid input. The given input string
          cannot be empty.'

    - Can the given input NOT be of a string data type?
        - No. It must be a string.

    - If given an input of a different data type than 'string' (i.e. - integer,
      floating point number, list, etc.), how would you handle it?
        - Return a string that says, "Invalid input. The given input must be of
          'string' data type."

PHASE II: devise a PLAN

- First Pass Solution: 

    (1) Define a function that takes in a single input, 'txt', and returns a
    single output, 'is_correct'.

    (2) Validate the given input to ensure that it is of 'string' data type.

        (a) If it is not of a 'string' data type, return a string that says,
        "Invalid input. The given input must be of 'string' data type."

        (b) Otherwise, do nothing.

    (3) Declare a var, 'is_correct', and initialize it with 'False' (Boolean
    value).

    (4) Declare another var, 'txt_split_list', and initialize it with the value
    of "txt.split(' ')".

    (5) Validate the length of 'txt_split_list' to ensure that there is an odd
    number of elements in it.

        (a) If there is an EVEN number of elements in it, return the value of 
        'is_correct' (which should still be False).

        (b) If there is an ODD number of elements in it, do nothing.

    (6) Declare a var, 'txt_nums_list', and initialize it with an empty pair of
    square brackets.
    
    (7) Declare a var, 'txt_operators_list', and initialize it with an empty pair of
    square brackets.  

    (8) Iterate through the 'txt_split_list' with a 'for' loop.

        (a) Declare a var, 'element', and set its value equal to the element 
        (from 'txt_split_list') being iterated on.
        
        (b) If 'element' is of 'integer' data type, append it to 'txt_nums_list'.
        
        (c) Otherwise, append 'element' to the 'txt_operators_list'.

    (9) Declare a var, 'valid_operators_cache', and initialize it with the 
    following values: 
        {
            '<': True,
            '>': True,
            '==': True,
            '<=': True,
            '>=': True,
            '!=': True
        }
        
    (10)



PHASE III: EXECUTE the plan PHASE IV: REFLECT on/REFACTOR the plan
"""

def correct_signs(txt):
    return txt

print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))