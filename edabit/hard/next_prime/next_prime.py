"""
NEXT PRIME

Given an integer, create a function that returns the next prime number. If the
number is prime, return the number itself.

Examples:
    - next_prime(12) -> 13
    - next_prime(24) -> 29
    - next_prime(11) -> 11
"""

"""
PHASE I: UNDERSTANDING THE PROBLEM

- Objective:
    - Write an algorithm that takes in a single input (an integer) and returns
      the next prime number (an integer).

- Expected Input:
    - Number of: 1
    - Data Type: integer
    - Var Name: 'input_num'
    
- Expected Output:
    - Number of: 1
    - Data Type: integer
    - Var Name: 'next_prime_num'
    
- Constraints:
    - Can the 'input_num' be negative?
        - No.
    - Can the 'input_num' be a floating point number?
        - No.
    - Can the 'input_num' be 0?
        - No.
    - Can the 'input_num' be 1?
        - No.
        - The lowest possible input is 2.

PHASE II: DEVISING A PLAN
    - Brute Force Solution
        (1) Define a helper function that checks to see if a number is prime or not.
        (2) Define a function that takes in 1 input (an integer) and returns 1
            output (an integer representing the next prime number).
        (3) Evaluate the input to make sure it is valid.
            (a) If input < 2, return a string telling user to input a different input.
            (b) If input >= 2, continue on with finding the next prime number.
        (4) Declare a var, 'next_prime_num', and initialize it with a value of 0.
        (5) Call the helper function to evaluate whether or not the 'input_num' is
            prime.
            (a) If it is, set the 'next_prime_num' var equal to it and return it.
            (b) If it isn't, do nothing.
        (6) Use a 'while' loop that begins iterating upwards from the 'input_num' as
            a starting point and continues iterating as long as 'next_prime_num' == 0.
        (7) For each iterated on number, call the helper function to evaluate
            whether or not the 'input_num' is prime.
            (a) If it is, set the 'next_prime_num' var equal to it and return it.
            (b) If it isn't, continue iterating through subsequent numbers and
                evaluating for the next prime number.    
        
PHASE III: EXECUTING THE PLAN (PLEASE SEE BELOW)

PHASE IV: REFLECTING ON/REFACTORING THE PLAN
    - Brute Force Solution
        - Asymptotic Analysis:
            - Time Complexity: O(n^2) -> "quadratic"
"""

def check_prime(num):
    is_prime = False
    
    factors = []
    
    num_of_factors = 0
    
    i = 1
    while i <= num:
        if num % i == 0:
            factors.append(i)
            num_of_factors += 1
        i += 1

    if num_of_factors == 2:
        is_prime = True
        return is_prime
    else:
        return is_prime

def get_next_prime(input_num):
    next_prime_num = 0
    
    if input_num < 2:
        return "Invalid input. Please enter an integer greater than 1."
    
    check_prime_input_num = check_prime(input_num)
    
    if check_prime_input_num == True:
        next_prime_num = input_num
        return next_prime_num
    
    j = input_num + 1
    while next_prime_num == 0:
        possible_next_prime = check_prime(j)
        
        if possible_next_prime == True:
            next_prime_num = j
            return next_prime_num
        
        j += 1

    
    
        
            

