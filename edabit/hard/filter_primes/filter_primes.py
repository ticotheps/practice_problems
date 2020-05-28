"""
FILTER PRIMES FROM A LIST

Create a function that takes in a list and returns a new list containing only
prime numbers.

Examples:
    - filter_primes([7, 9, 3, 9, 10, 11, 27]) -> [7, 3, 11]
    - filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) -> [10007, 1009]
    - filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091,
    1093, 1097]) -> [1009, 3, 61, 1087, 1091, 1093, 1097]
"""

"""
PHASE I: UNDERSTANDING THE PROBLEM

Objective: 
    - Write an algorithm that takes in a single input (a Python list) and
    filters out all of the non-prime numbers to return a new Python list as the
    single output.
    
Expected Input(s):
    - Number Of: 1
    - Data Type: Python list
    - Var Name: 'num_list'
    
Expected Output(s):
    - Number Of: 1
    - Data Type: Python List
    - Var Name: 'filtered list'
    
Constraints:
    - Provided Notes:
        - New list must maintain the order of primes as they first appear in the
        original list.
    - Can the numbers in the input list be negative?
        - No, because prime numbers must be positive.
    - Can the numbers in the input list be floating point numbers?
        - No, because prime numbers must be whole integers.
    - Can 0 exist as a number in the input list?
        - Yes, but 0 is NOT a prime number.
    - Can 1 exist as a number in the input list?
        - Yes, but 1 is NOT a prime number.
    
    
PHASE II: DEVISING A PLAN
PHASE III: EXECUTING THE PLAN
PHASE IV: REFLECTING ON/REFACTORING THE SOLUTION
"""

