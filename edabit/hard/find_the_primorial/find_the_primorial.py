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
    (1) Create a helper function that will check if a number is prime or not.

    (2) Create a helper function that will take in a 'max_primes' argument
    and will generate 'max_primes' number of prime numbers to be added into
    a 'primes' list that will be returned as the output.

    (3) Define a function that takes in a 'num_of_primorial' input (integer data type) and
    returns a 'primorial' output (integer data type).
    
    (4) Declare a var, 'primes_list', that will be equal to calling the helper function from step 1 and pass in 'num_of_primorial' as the argument.
    
    (5) Declare a var, 'primorial', that will be returned as the output. Initialize it with a value of '1' (integer).
    
    (6) Use a 'for' loop to iterate through all the elements in 'primes_list'.
    
        (a) Multiply the 'primorial' value by each element of 'primes_list'.
        
    (7) Return the value of 'primorial'.
    
PHASE III - EXECUTE (PLEASE SEE BELOW)

PHASE IV - REFLECT/REFACTOR

Brute Force Solution:
    - Asymptotic Analysis:
        - Time Complexity: O(n^2) -> 'quadratic'
        - Space Complexity: O(1) -> 'constant'
        
    - Could this solution be improved?
        - Yes.
    - How?
        - Use a python dictionary to cache already-calculated primorials. Then, when given an input, first lookup the input in the cache to see if the input already exists. If not, retrieve the next closest key from the cache and use the value as a starting point to minimize the amount calculations required to find the primorial.
    - What is the new asymptotic analysis?
        - Time Complexity: O(n log n) -> 'linearithmic'
        - Space Complexity: O(n) -> 'linear'
"""

def check_prime(num): 
    is_prime = True
    
    if num < 2:
        is_prime = False
        return is_prime
    
    num_of_factors = 2
    
    factors = [1, num]
    
    for j in range(2, num):
        if num % j == 0:
            num_of_factors += 1
            is_prime = False
            return is_prime
    return is_prime

def generate_primes_list(max_primes):
    primes_list = []
    num_of_primes = 0
    i = 2
    
    while num_of_primes != max_primes:
        possible_prime = check_prime(i)
        if possible_prime == True:
            num_of_primes += 1
            primes_list.append(i)
        i += 1
            
    return primes_list
    
def get_primorial(num_of_primorial):
    primes_list = generate_primes_list(num_of_primorial)
    primorial = 1
    
    for element in primes_list:
        primorial *= element
        
    return primorial