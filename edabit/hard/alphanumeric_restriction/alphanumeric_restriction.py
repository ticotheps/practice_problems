"""
ALPHANUMERIC RESTRICTION

Create a function that returns True if the given string has any of the
following:

    - Only letters and no numbers.
    - Only numbers and no letters.
    
If a string has both numbers and letters, or contains characters which don't fit
into any category, return False.

Examples:
    - alphanumeric_restriction("Bold") ➞ True

    - alphanumeric_restriction("123454321") ➞ True

    - alphanumeric_restriction("H3LL0") ➞ False

    - alphanumeric_restriction("ed@bit") ➞ False
    
Notes:
    - Any string that contains spaces or is empty should return False.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND Phase ******
- Objective:
    - Write an algorithm that takes in a single string input and returns a
      single Boolean value as the output.
    - In order for the algorithm to return True, the given string must either:
        (a) contain only letters and no numbers.
                        or
        (b) contain only numbers and no letters.
        
- Expected Input(s):
    - Number Of: 1
    - Data Types: string
    - Var Names: "s"
    
- Expected Output(s):
    - Number Of: 1
    - Data Types: Boolean value (True or False)
    - Var Names: "meets_criteria"
    
- Edge Cases & Constraints
    - Can a given input string be empty or contain only spaces?
        - Yes. However, you should return False for those instances.

****** PLAN Phase ******
- First Pass Solution:

    (1) Define a function that takes in a single input, "s", and returns a
    single output, "meets_criteria".
    
    (2) Declare a var, "meets_critera", and initialize it with a Boolean value
    of False.
    
    (3) Use an "if" statement and the ".isalpha()" method to determine if all of
    the characters in the given input string are alphabetic.
    
        (a) If all the characters are alphabetic, set "meets_criteria" to True.
        
        (b) Otherwise, do nothing.
    
    (4) Use an "elif" statement and the ".isnumeric()" method to determine if all
    of the characters in the given input string are numeric.
    
        (a) If all the characters are numeric, set "meets_criteria" to True.
        
        (b) Otherwise, do nothing.
    
    (5) Return the value of "meets_criteria".

****** EXECUTE Phase ****** (Please see below)



"""


def alphanumeric_restriction(s):
    pass

print(alphanumeric_restriction("Bold"))  # True

"""
****** REFLECT/REFACTOR ******

"""