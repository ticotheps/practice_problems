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
        - Return a string that says, "Invalid input. The given input must of
          'string' data type."
    
PHASE II: device a PLAN
PHASE III: EXECUTE the plan
PHASE IV: REFLECT on/REFACTOR the plan
"""

def correct_signs(txt):
    return txt

print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))