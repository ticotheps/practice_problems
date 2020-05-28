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
# helper function that checks the prime status of a given number
def check_prime(num):
    # print(f"\n----------num = {num}----------")
    
    # Keep track of 'prime_status' of 'num'. Initialize this var with False.
    is_prime = False
    # print(f"INITIAL is_prime = {is_prime}")
    
    # Keep track of the factors of 'num'.
    factors = []
    # print(f"INITIAL factors = {factors}")

    # Keep track of the number of factors that 'num' has.
    num_of_factors = 0
    # print(f"INITIAL num_of_factors = {num_of_factors}")
    
    # Evaluate for a valid given input 'num'
    if num < 2 or type(num) == float:
        # print(f"Sorry. {num} is not a valid input. Try a positive integer instead.\n")
        return is_prime
    
    # Use a 'while' loop to iterate through a list of numbers that has a
    #   start point of 1 and an end point of num+1 AS LONG AS 'num_of_factors' is
    #   less than or equal to 2.
    i = 1
    while i <= num + 1:
        # Evaluate whether or not 'i' is a factor of 'num'.
        # If 'i' IS a factor of 'num'...
        if num % i == 0:
            # print(f"{i} is a factor of {num}")
            
            # ...add it to the list of factors for 'num'
            factors.append(i)
            # print(f"**UPDATED** factors = {factors}")
            
            # ...increase the count of factors for 'num'
            num_of_factors += 1
            # print(f"**UPDATED** num_of_factors = {num_of_factors}")
        
        # Increase the iterated number, 'i', by 1.
        i += 1
            
        # Evaluate whether or not 'num' is now prime.
        if num_of_factors > 2:
            # print(f"**UPDATED** is_prime = {is_prime}")
            # print(f"{num} is NOT a prime number\n")
            return is_prime
        
    # If the 'while' loop completes execution and 'num_of_factors' is equal to
    #   2, 'num' is a prime number, so update 'is_prime' to True.
    if num_of_factors == 2:
        # print(f"**UPDATED** is_prime = {is_prime}")
        # print(f"{num} IS a prime number!\n")
        is_prime = True
        
    # Return the value of 'is_prime'.
    return is_prime

# print(check_prime(1)) # -> False
# print(check_prime(2)) # -> True
# print(check_prime(3)) # -> True
# print(check_prime(4)) # -> False
# print(check_prime(5)) # -> True
# print(check_prime(6)) # -> False
# print(check_prime(7)) # -> True
# print(check_prime(8)) # -> False
# print(check_prime(9)) # -> False
# print(check_prime(10)) # -> False
# print(check_prime(11)) # -> True
        
# Define a main function that will filter out non-prime integers from the given
#   input list and return a new, filtered-version of that given list with ONLY
#   prime numbers as elements (with an unchanged order from the original list).
def filter_primes(num_list):
    # print(f"num_list = {num_list}")
    
    filtered_list = []
    
    for i in num_list:
        # print(f"i = {i}")
        
        possible_prime = check_prime(i)
        
        if possible_prime == True:
            filtered_list.append(i)
            # print(f"filtered_list = {filtered_list}")
    
    return filtered_list
