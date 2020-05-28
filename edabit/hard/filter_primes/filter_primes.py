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
    
Defining Terms:
    - 'PRIME': 
        - a positive integer whose only factors are 1 and the integer itself.
    
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

Brute Force Solution
    (1) Define a helper function, 'check_prime()', that will determine the prime
    status of a given number.
    
    (2) Define another function, 'filter_primes()', that will take in a single list of integers, remove any non-prime integers from that list, and return the filtered-version of the original list (with the original ordering of the integers intact).
    
    (3) Declare a var, 'filtered_list', that will be returned as the output. Initialize this var with a value of '[]'.
    
    (4) Use a 'for' loop to iterate through the given input list to determine whether or not each element is prime.
    
        (a) If the element is prime, append it to the 'filtered_list'.
        
        (b) If the element is NOT prime, do nothing.
        
    (5) Return the value of 'filtered_list'.

PHASE III: EXECUTING THE PLAN (Please see Brute Force Solution below)

PHASE IV: REFLECTING ON/REFACTORING THE SOLUTION

Brute Force Solution
    - Asymptotic Analysis:
        - Time Complexity: O(n^2) -> 'quadratic'
        - Space Complexity: O(1) -> 'constant'
"""
def check_prime(num):
    is_prime = False
    factors = []
    num_of_factors = 0
    
    if num < 2 or type(num) == float:
        return is_prime

    i = 1
    while i <= num + 1:
        if num % i == 0:
            factors.append(i)
            num_of_factors += 1

        i += 1

        if num_of_factors > 2:
            return is_prime

    if num_of_factors == 2:
        is_prime = True

    return is_prime

def filter_primes(num_list):    
    filtered_list = []
    
    for i in num_list:
        # print(f"i = {i}")
        
        possible_prime = check_prime(i)
        
        if possible_prime == True:
            filtered_list.append(i)
    
    return filtered_list
