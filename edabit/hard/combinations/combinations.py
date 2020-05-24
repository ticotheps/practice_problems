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
PHASE III: EXECUTING THE PLAN
PHASE IV: REFLECT ON/REFACTOR THE PLAN
"""