"""
RECURSION: LENGTH OF A STRING

Instructions:
    - Write a function that returns the length of a string. Make your function
recursive.

Examples:
    - length('apple') -> 5
    - length('make') -> 4
    - length('a') -> 1
    - length('') -> 0
"""

"""
----- 4 Phases of The U.P.E.R. Problem-Solving Framework -----

PHASE I: UNDERSTAND [the problem]

- Objective:
    - Write a recursive algorithm that takes in a single input string and
    returns a single output, which is the length of the string.
    
- Definitions:
    - Recursive:
        - "a function that calls itself from within its own function
        body."
        - "something that defines itself in terms of itself."
    - Anatomy of a Recursive Function:
        (1) A recurrence relation
            - A sequence based on a rule that gives the next term as a function
            of the previous term(s).
        (2) A termination condition (AKA "base case")
            - The condition at which recursion will stop.
            
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): string
    - Var Name(s): 'txt'
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'len_of_txt'
    
- Edge Cases & Constraints:
    - Can the given input be a non-string data type?
        - No. It MUST be a string.
    - Can the given input be an empty string?
        - Yes. The length of the given string would be 0.

-------------------------------------------------------------------------------

PHASE II: [devise a] PLAN

-------------------------------------------------------------------------------

PHASE III: EXECUTE [the plan]

-------------------------------------------------------------------------------

PHASE IV: REFLECT ON/REFACTOR [the plan]
"""

def length(txt):
    len_of_txt = 0
    print(f"len_of_txt = {len_of_txt}")
    
    return len_of_txt

print(length('apple'))  # 5
print(length('make'))  # 4
print(length('a'))  # 1
print(length(''))  # 0