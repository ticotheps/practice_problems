"""
THE MUSEUM OF INCREDIBLY DULL THINGS

A museum wants to get rid of some exhibitions. Katya, the interior architect,
comes up with a plan to remove the most boring exhibitions. She gives them a
rating, and removes the one with the lowest rating. Just as she finishes rating
the exhibitions, she's called off to an important meeting. She asks you to write
a program that tells her the ratings of the items after the lowest one is
removed.

Create a function that takes a list of integers and removes the smallest value.

Examples:
    - remove_smallest([1, 2, 3, 4, 5]) -> [2, 3, 4, 5]
    - remove_smallest([5, 3, 2, 1, 4]) -> [5, 3, 2, 4]
    - remove_smallest([2, 2, 1, 2, 1]) -> [2, 2, 2, 1]
    
Notes:
    - Don't change the order of the left over items.
    - If you get an empty list, return an empty list (i.e. - "[]" -> "[]").
    - If there are multiple items with the same value, remove the item with the
    lower index (i.e. - look at the 3rd example above).
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

***** U = UNDERSTAND Phase *****

- Objective:
    - Write an algorithm that takes in a single input list of integers and removes the
      smallest integer (or the duplicate of the smallest with the smallest index
      if there are more than one), returning the revised list (without the
      smallest integer included) as a single output.
      
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Names: 'lst'
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Names: 'new_lst'
    
Edge Cases & Constraints:
    - Can the input list be empty?
        - Yes, but you must return an empty list ("[]") if the given input is an
        empty list.
    - Can the numbers in the given input list be negative?
        - No. These are "ratings" so they must be positive.
    - Can the numbers in the given input list be floating point numbers?
        - No. They must be whole integers
    

***** P = PLAN Phase *****
***** E = EXECUTE Phase *****
***** R = REFLECT/REFACTOR Phase *****
"""

def remove_smallest(lst):
    pass

