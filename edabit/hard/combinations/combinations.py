"""
COMBINATIONS

Create a function that takes a variable number of groups of items and returns the number
of ways that the items can be arranged, with one item from each group. Order does not matter.
"""

"""
PHASE I: UNDERSTANDING THE PROBLEM

- Objective:
    - Write an algorithm that takes in multiple arguments (of integer data types),
      representing the number of "items" in that group, and then returns a
      single output (of integer data type), representing the different number of
      possible combinations in which the individual items (from each group) could be
      combined could be combined with one another.
      
- Expected:
    - Inputs:
        - Number: multiple
        - Types: integers
        - Names: arg1, arg2, ...
        
    - Outputs:
        - Number: 1
        - Type: integer
        - Name: 'num_of_combinations'
        
- Constraints:
    - Can the inputs be negative integers?
        - No, because each input represents a separate "group" and the number
          itself represents the number of arbitrary "items" within that group.
    - Can the inputs be floating point numbers?
        - No. because each input represents a separate "group" and the number
          itself represents the number of arbitrary "items" within that group.
    - Can the inputs be empty strings?
        - No, the inputs MUST be positive integers.
        
PHASE II: DEVISING A PLAN

- Brute Force Solution:
    (1) Define a function that can take in any number of arguments (i.e. - *args).
    (2) Declare a var that will be returned as our output.
    (3) Iterate over all the arguments in *args using a 'for' loop.
    (4) Multiply the value of 'num_of_combinations' by each argument to get the
    total number of possible combinations (where order doesn't matter). 
    (5) Return the value of the var declared in step 2.

PHASE III: EXECUTING THE PLAN (PLEASE SEE BELOW)

PHASE IV: REFLECT ON/REFACTOR THE PLAN

- Asymptotic Analysis:
    - Time Complexity:
        - O(n) -> 'linear'
        - Due to 'for' loop iterating through each arg.
    - Space Complexity:
        - O(1) -> 'constant'
        - No other memory outside of the given inputs is required to solve the
          problem.
"""

def get_combinations(*args):
    num_of_combinations = 1
    for item in args:
        if item == 0:
            item = 1

        num_of_combinations *= item
        
    return num_of_combinations