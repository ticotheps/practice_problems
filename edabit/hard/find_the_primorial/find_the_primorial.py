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
"""

def check_prime(num): 
    print(f"-------------- num = {num} ---------------")  
    is_prime = True
    print(f"\nis_prime = {is_prime}")
    
    if num < 2:
        print(f"\n{num} is not a valid input")
        is_prime = False
        return is_prime
    
    num_of_factors = 2
    print(f"num_of_factors = {num_of_factors}")
    
    factors = [1, num]
    print(f"factors = {factors}")
    
    for j in range(2, num):
        print(f"j = {j}")
        if num % j == 0:
            print(f"{j} is a factor of {num}")
            num_of_factors += 1
            print(f"{num} now has {num_of_factors} factors and is NOT considered prime")
            is_prime = False
            return is_prime
    
    print(f"{num} only has {num_of_factors} so it IS considered prime")
    return is_prime

print(check_prime(1)) # -> False
print(check_prime(2)) # -> True
print(check_prime(3)) # -> True
print(check_prime(4)) # -> False
print(check_prime(5)) # -> True



def generate_primes_list(max_primes):
    print(f"max_primes = {max_primes}")
    
    # Declare a var that will hold a list of generated prime numbers
    primes_list = []
    print(f"primes_list = {primes_list}")
    
    # Declare a var representing the current number of generated prime numbers
    num_of_primes = 0
    print(f"num_of_primes = {num_of_primes}")
    
    # Use a 'while' loop to continue generating prime numbers as long as
    # 'num_of_primes' is NOT equal to 'max_primes'.
    i = 2
    while num_of_primes != max_primes:
        print(f"i = {i}")
        
        # call 'check_prime()' on 'i'
    
    
    
# print(generate_primes_list(3))  # -> [2, 3, 5]
    