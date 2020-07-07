"""
NTH SMALLEST ELEMENT

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the FIRST smallest, the second smallest element is the
second smallest, etc.).

Examples:
    - nth_smallest([1, 3, 5, 7], 1) -> 1
    - nth_smallest([1, 3, 5, 7], 3) -> 5
    - nth_smallest([1, 3, 5, 7], 5) -> None
    - nth_smallest([7, 3, 5, 1], 2) -> 3

Notes:
    - 'n' will always be >= 1.
    - Each number in the array will be distinct (there will be a clear
    ordering).
    - Given an out of bounds parameter (e.g. a list is of size 'k'), and you are
    asked to find the m < k smallest element, return None.
"""

"""
The U.P.E.R. Problem-Solving Framework

***** U = UNDERSTAND *****
- Objective:
    - Write an algorithm that takes in two inputs, "lst" (an unsorted list) and
      "n" (the desired index when first input is sorted), and returns a single
      output, "nth_smallest".
      
- Expected Inputs:
    - Number Of: 2
    - Data Types: list, integer
    - Var Names: "lst", "n"
    
- Expected Outputs:
    - Number Of: 1
    - Data Types: integer or None
    - Var Name: "nth_smallest"
    
- Edge Cases & Constraints:
    - Can the input list include elements that are not of integer data type?
        - No. The elements of any given list must be of integer data type.
    - Can the input list include 0 elements?
        - No. The given input list will have at least 1 element.
    
***** P = PLAN *****
- Brute Force Solution:
    (1) Define a function that takes in 2 parameters, "lst" and "n", and 
    returns a single output, "nth_smallest".\
    
    (2) Declare a var, "nth_smallest", and initialize it with a value of None.
    
    (3) Sort the given input list using the ".sorted()" function (this returns 
    a new sorted copy of the given input list unlike ".sort()" would do) and 
    set it equal to a new var, "sorted_lst".
    
    (4) Evaluate the length of "sorted_lst".
    
        (a) If the length of "sorted_lst" is greater than or equal to "n", return 
        the "n" element from "sorted_lst".
        
        (b) If the length of "sorted_lst" is less than "n", return None.
    

***** E = EXECUTE ***** (please see below)
"""
def nth_smallest(lst, n):
    nth_smallest = None
    sorted_lst = sorted(lst)
    
    if len(sorted_lst) >= n:
        nth_smallest = sorted_lst[n-1]
    
    return nth_smallest

"""
***** R = REFLECT/REFACTOR *****
- Asymptotic Analysis:
    - Brute Force Solution:
        - Time Complexity: O(n log n)
        - Space Complexity: O(n)
"""