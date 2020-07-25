"""
FIND THE MISSING NUMBER

Create a function that takes in a list of numbers between 1 and 10 (excluding
one number) and returns the missing number.

- Examples:
    - missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) -> 5
    - missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) -> 10
    - missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]) -> 7
    
- Notes:
    - The list of numbers will be unsorted (not in order).
    - Only one number will be missing.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND Phase ******
- Objective:
    - Write an algorithm that takes in a list of numbers that will contain 9
      elements (some integers from 1 - 10) and will return the single integer
      that is missing from the list (in order to complete the list of integers
      from 1 through 10).
      
- Expected Input(s):
    - Number Of:        1
    - Data Type(s):     list
    - Var Name(s):      "lst"
    
- Expected Output(s):
    - Number Of:        1
    - Data Type(s):     integer
    - Var Name(s):      "missing_int"
    
- Edge Cases & Constraints:
    - Can the given input list contain less or more than 9 elements?
        - No. It must only ever contain exactly 9 elements.
    - Is the given input list provided in sorted order?
        - No. It can be unsorted.
    - Can the given input list contain non-integer values for its elements?
        - No. All elements must be: of the integer data type, without duplicates,
          and ranging from 1-10.

****** PLAN Phase ******
- First Pass Solution:
    (1) Define a function, "missing_num()", that takes in a single input list
    (of numbers ranging from 1-10) and returns a single integer (which
    represents the missing integer from the list of integers ranging from 1-10).
    
    (2) Declare a var, "missing_int", and initalize it with a value of 1 (of
    integer data type).
    
    (3) Declare a var, "sorted_lst", and initialize it with a sorted version of
    the given input list using the ".sorted()" method.
    
    (4) Use a 'for' loop and the 'enumerate()' method to iterate through the 
    "sorted_lst", where the iterators will be "element" and "index"...
    
        (a) Define a var, "place_in_lst", and initialize it with a value of 
        "index + 1".

        (b) If the "element" is NOT EQUAL TO the "index+1", then:
            
            (i) add "place_in_lst" to the value of "missing_int".
        
        (c) Else, do nothing.
        
    (5) Return the value of "missing_int".

****** EXECUTE Phase ****** (Please see below)
"""

def missing_num(lst):
    pass

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))  # 5