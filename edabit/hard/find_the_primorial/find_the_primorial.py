"""
FIND THE PRIMORIAL

A 'Primorial' is a product of the first n prime numbers (e.g. - 2 x 3 x 5 = 30).
2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30
or 'Primorial' = 30.

Create a function that returns the Primorial of a number.

Examples:
    - get_primorial(1) -> 2
    - get_primorial(2) -> 6
    - get_primorial(8) -> 9699690
"""

"""
U.P.E.R. Problem-Solving Framework

PHASE I - UNDERSTAND

Defining Terms:
    - 'Primorial': the product of 'n' number of consecutive prime numbers,
    beginning with 2 as the first prime number.

Objective:
    - Write an algorithm that takes in a single input, 'num', and returns a
    single output, 'primorial', for that number.
    
Expected Input(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'num_of_primorial'
    
Expected Output(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'primorial'
    
Constraints:
    - Can the input 'num' be negative?
        - No, because it refers to a specific number of prime numbers in a sequence
        and prime numbers must be positive.
    - Can the input 'num' be a floating point number?
        - No, because it refers to a specific number of prime numbers in a sequence
        and prime numbers must be whole.
    - Can the input 'num' be null?
        - No.
    
PHASE II - PLAN

Brute Force Solution:
    (1) Create a helper function that will take in a 'max_primes' argument
    and will generate 'max_primes' number of prime numbers to be added into
    a 'primes' list that will be returned as the output.

    (2) Define a function that takes in a 'num_of_primorial' input (integer data type) and
    returns a 'primorial' output (integer data type).
    
    (3) Declare a var, 'prime_list', that will be equal to calling the helper function from step 1 and pass in 'num_of_primorial' as the argument.
    
    (4) Declare a var, 'primorial', that will be returned as the output. Initialize it with a value of '1' (integer).
    
    (5) Use a 'for' loop to iterate through all the elements in 'prime_list'.
    
        (a) Multiply the 'primorial' value by each element of 'prime_list'.
        
    (6) Return the value of 'primorial'.
    
PHASE III - EXECUTE (PLEASE SEE BELOW)

PHASE IV - REFLECT/REFACTOR
"""