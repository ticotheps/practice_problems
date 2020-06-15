"""
FACTORIAL OF A POSITIVE INTEGER

- Write a function that takes a positive integer and return its factorial.

- Examples:
    - factorial(4) -> 24
    - factorial(0) -> 1
    - factorial(9) -> 362880
    
- Notes:
    - The factorial of 0 is 1.
    - The factorial of any positive integer, Z, is Z * (Z-1) * (Z-2) * ... * 1.
        - i.e. - factorial of 3 is (3 * 2 * 1 = 6)
"""

"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND [the problem]

- Objective:
    - Write an algorithm that takes in a single input (integer data type) and
      returns a single output (integer data type), which is the "factorial" of
      the given input.

- Key Terms:
    - "factorial":
        - the product of a positive integer and all the positive integers below
          it.

- Expected Input(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'Z'

- Expected Input(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'factorial'

- Constraints:
    - Can the input be a negative integer?
        - No.
    - Can the input be a floating point number?
        - No.
    - Can the input be null?
        - No. The input MUST be a positive integer.

PHASE II: [Devise a] PLAN

- First-Pass Solution: (1) Define a function, 'factorial()', that takes in a
    single input (integer data type), 'Z', and returns a single output (integer
    data type), 'factorial', which will be the factorial of the given input.

    (2) Declare a var, 'factorial', that will be returned as the output.
    Initialize it with a value of 1

    (3) If 'Z' is LESS THAN 0, return a string that says, "Invalid input. Please
    try a positive integer instead."

    (4) If 'Z' is equal to 0, return the value of 'factorial'.
    
    (5) If 'Z' is of 'float' data type, return a string that says, "Invalid
    input. Please try a positive integer instead."

    (6) Use a 'for' loop to iterate through a range of numbers (1 -> Z)...

        (a) Declare a var, 'int_below_z', and set it equal to the iterator used
        in the 'for' loop.
        
        (b) Multiply the value of 'factorial' by the value of 'int_below_z' and
        set that value equal to 'factorial'.
        
    (7) Return the value of 'factorial'.

PHASE III: EXECUTE [the plan]
    - First-Pass Solution (PLEASE SEE BELOW)

PHASE IV: REFLECT ON/REFACTOR [the plan/solution]
    - First-Pass Solution:
        - Asymptotic Analysis:
            - Time Complexity:
                - O(n) -> 'linear'
            - Space Complexity:
                - O(1) -> 'constant'
        - Can this solution be optimized?
            - Yes.
        - How?
    - Use a 'factorial_cache' object that stores key/value pairs where the
    'keys' are previously inputs, 'Z', and the 'values' are previously
    calculated factorials for the corresponding 'keys'.
"""

def factorial(Z):
    factorial = 1
    
    if Z < 0 or type(Z) == float:
        return "Invalid input. Please try a positive integer instead."
    
    elif Z == 0:
        return factorial
    
    else:
        for i in range(1, Z + 1):
            int_below_z = i
            factorial *= int_below_z
    
    return factorial

print(factorial(-2))    # "Invalid input. Please try a positive integer instead."
print(factorial(2.133)) # "Invalid input. Please try a positive integer instead."
print(factorial(4))     # 24
print(factorial(0))     # 1
print(factorial(9))     # 362880


# Declare a cache object to store previously calculated factorials.
factorial_cache = {"2":2, "3":6, "5":120, "7":5040}
print(f"factorial_cache = {factorial_cache}")

# Define a function that optimizes the time complexity for your first-pass solution.
def optimized_factorial(Z):
    print(f"\nZ = {Z}")
    
    # Declare a var that keeps track of the factorial of 'Z'.
    factorial = 1
    print(f"*INITIAL* factorial = {factorial}")
    
    # Evaluate for a valid input data type of 'int'.
    if Z < 0 or type(Z) == float:
        return "Invalid input. Please try a positive integer instead."
    
    # Evaluate for a case where 'Z' is 0.
    elif Z == 0:
        return factorial
    
    else:
        # Declare a var that keeps track of the largest cached KEY that we can
        # can use to help us reduce the number of calculations to be done.
        largest_cached_Z = 0
        print(f"*INITAL* largest_cached_Z = {largest_cached_Z}")
        
        # Declare a var that keeps track of the largest cached [pre-calculated]
        # VALUE that we can use to help reduce the number of calculations.
        precalculated_factorial = 0
        print(f"*INITAL* precalculated_factorial = {precalculated_factorial}")
        
        # Declare a var that keeps track of the new 'Z' value based on the what
        # key we utilize from the 'factorial_cache' object.
        new_Z_min = 0
        print(f"*INITAL* new_Z_min = {new_Z_min}")
        
        # Compare each key in the 'factorial_cache' object to 'Z'.
        for key in factorial_cache:
            key_int = int(key)
            print(f"\nkey_int = {key_int}")
            
            # Find the largest key in the 'factorial_cache' object that is LESS
            # than 'Z'.
            if key_int < Z and key_int > largest_cached_Z:
                print(
                    f"{key} is less than {Z} so we could use the previously "
                    f"calculated factorial for {key} (which is "
                    f"{factorial_cache[key]})."
                )
                
                # Set current 'largest_cached_Z' to the value of 'k' (as an 
                # integer).
                largest_cached_Z = key_int
                print(f"**UPDATED** largest_cached_Z = {int(largest_cached_Z)}")
                
                # Set current 'precalculated_factorial' to the value associated 
                # with 'largest_cached_Z' key from the 'factorial_cache' object.
                precalculated_factorial = factorial_cache[key]
                print(f"**UPDATED** precalculated_factorial = {precalculated_factorial}")
                
                # Multiply the value of 'precalculated_factorial' by the value 
                # of 'factorial'.
                factorial = precalculated_factorial
                print(f"**UPDATED** factorial = {factorial}")
                
                # Set the value of 'new_Z' to the difference of 'Z' and
                # 'largest_cached_Z'.
                new_Z_min = largest_cached_Z + 1
                print(f"**UPDATED** new_Z_min = {new_Z_min}")
                
        
        for i in range(new_Z_min, Z + 1):
            multiplier = i
            print(f"multiplier = {multiplier}")
            factorial *= multiplier
            print(f"***CURRENT*** factorial = {factorial}")
            print(f"(last 'for' loop) **UPDATED** factorial = {factorial}")
    
    return factorial

# print(optimized_factorial(-2))    # "Invalid input. Please try a positive integer instead."
# print(optimized_factorial(2.133)) # "Invalid input. Please try a positive integer instead."
# print(optimized_factorial(0))     # 1
print(optimized_factorial(4))     # 24
# print(optimized_factorial(9))     # 362880
# print(optimized_factorial(12))     # 479001600