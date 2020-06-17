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

- [Iterative] Brute Force Solution:
    (1) Define a function that takes in a single string input and returns the
    length of the given input string as an integer.
    
    (2) Declare a variable, 'len_of_txt', and initialize it with an integer 
    value of 0.
    
    (3) Find the length of 'txt' by calling the '.len()' method on 'txt' and
    then set the value of 'len_of_txt' equal to the resulting length.
    
    (4) Return the value of 'len_of_txt'.
    
    
- [Recursive] Brute Force Solution:
    (1) Define a function that takes in a single string input and returns the
    length of the given input string as an integer.
    
    (2) Define a base case where if 'txt' is an empty string, return 0.
    
    (3) Return 1 and make a recursive call to the 'length()' function, passing
    in the range of indices for the given input string where the 'start' is the
    next index and the 'stop' is the end of the string.

-------------------------------------------------------------------------------

PHASE III: EXECUTE [the plan] (Please See Below)

-------------------------------------------------------------------------------

PHASE IV: REFLECT ON/REFACTOR [the plan]

- Asymptotic Analysis:

    - Iterative Solution:
        - Time Complexity: O(n) -> 'linear'
        - Space Complexity: O(1) -> 'constant'
        
    - Recursive Solution:
        - Time Complexity: O(n) -> 'linear'
        - Space Complexity: O(nm) -> 'm' = maximum depth of recursion tree
"""
# ITERATIVE SOLUTION
# def length(txt):
#     len_of_txt = len(txt)
#     print(f"len_of_txt = {len_of_txt}")
    
#     return len_of_txt

# print(length('apple'))  # 5
# print(length('make'))  # 4
# print(length('a'))  # 1
# print(length(''))  # 0


# RECURSIVE SOLUTION
def length(txt):
    if txt == '':
        return 0
    return 1 + length(txt[1:])