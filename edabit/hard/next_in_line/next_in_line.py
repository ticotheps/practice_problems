"""
STAND IN LINE

Write a function that takes in a list and a number as arguments. Add the number
to the end of the list, then remove the first element of the list. The function
should then return the updated list.

- Examples:
    - next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]
    - next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]
    - next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]
    - next_in_line([], 6) ➞ "No list has been selected"
    
- Notes:
    - For an empty list input, return: "No list has been selected".
"""

"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND [the problem]

- Objective:
    - Write an algorithm that takes in two arguments, a list and an integer, and
    returns a single output, which is an updated list, where the first element
    of the original given input list is removed and the given integer input is
    added to the end of the original given input list.

- Expected Input(s):
    - Number Of: 2
    - Data Type(s): list, integer
    - Var Name(s): 'lst', 'num'

- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): 'new_lst'

- Edge Cases & Constraints:
    - What happens when the given input list is empty?
        - Return a string that says, "No list has been selected".
    - Can the given input integer be 0?
        - Yes
    - Can the given input integer be negative?
        - Yes.
    - Can the given input integer be a floating point number?
        - No. The given input must be an integer.


PHASE II: [devise a] PLAN

- Brute Force Solution: 

    (1) Define a function, 'next_in_line()', that takes in two inputs, 'lst'
    and 'num', and returns a single output, 'new_lst'.
    
    (2) Validate that the given input 'lst' has at least 1 element.
        (a) If 'lst' does NOT have a length of one or greater, return a string
        that says, "No list has been selected".

    (3) Declare a var, 'new_lst', and set it equal to the value of the given
    input 'lst'.
    
    (4) Use the '.pop(0)' method to remove the first item from 'new_lst'.
    
    (5) Use '.append()' method to add the given integer input to the end of
    'new_lst'.
    
    (6) Return the value of 'new_lst'.
    
PHASE III: EXECUTE [the plan] (Please see below)

PHASE IV: REFLECT ON + REFACTOR [the plan/solution]

"""

def next_in_line(lst, num):
    if len(lst) >= 1:
        new_lst = lst
        new_lst.pop(0)
        new_lst.append(num)
        return new_lst
    else:
        return "No list has been selected"