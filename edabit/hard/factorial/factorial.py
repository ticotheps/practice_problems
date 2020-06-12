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
    # print(f"\nZ = {Z}")
    
    factorial = 1
    # print(f"factorial = {factorial}")
    
    if Z < 0 or type(Z) == float:
        return "Invalid input. Please try a positive integer instead."
    
    elif Z == 0:
        return factorial
    
    else:
        for i in range(1, Z + 1):
            int_below_z = i
            # print(f"int_below_z = {int_below_z}")
            
            factorial *= int_below_z
            # print(f"*UPDATED* factorial = {factorial}")
    
    return factorial

# print(factorial(-2))    # "Invalid input. Please try a positive integer instead."
# print(factorial(2.133)) # "Invalid input. Please try a positive integer instead."
# print(factorial(4))     # 24
# print(factorial(0))     # 1
# print(factorial(9))     # 362880


# factorial_cache = {}
# print(f"factorial_cache = {factorial_cache}")

# def optimized_factorial(Z):
#     # print(f"\nZ = {Z}")
    
#     factorial = 1
#     # print(f"factorial = {factorial}")
    
#     if Z < 0 or type(Z) == float:
#         return "Invalid input. Please try a positive integer instead."
    
#     elif Z == 0:
#         return factorial
    
#     else:
#         largest_cached_Z = 0
        
#         for k in factorial_cache:
#             if int(k) < Z:
#                 print(f"{k} is less {Z} so we could potentially use the previously calculated factorial ({factorial_cache[k]}) for Z.")
                
#                 if int(k) > largest_cached_Z:
#                     largest_cached_Z = int(k)
        
#         print(f"largest_cached_Z = {largest_cached_Z}")
        
#         new_Z = Z - largest_cached_Z
#         print(f"new_Z = {new_Z}")
#         factorial *= factorial_cache[largest_cached_Z]
#         print(f"factorial = {factorial}")
        
#         for i in range(1, new_Z + 1):
#             int_below_z = i
#             # print(f"int_below_z = {int_below_z}")
            
#             factorial *= int_below_z
#             # print(f"*UPDATED* factorial = {factorial}")
    
#     if Z not in factorial_cache:
#         factorial_cache[Z] = factorial
#         print(f"factorial_cache[{Z}] = {factorial}")
#         print(f"*UPDATED* factorial_cache = {factorial_cache}")
        
    
#     return factorial

# # print(optimized_factorial(-2))    # "Invalid input. Please try a positive integer instead."
# # print(optimized_factorial(2.133)) # "Invalid input. Please try a positive integer instead."
# print(optimized_factorial(0))     # 1
# print(optimized_factorial(4))     # 24
# print(optimized_factorial(9))     # 362880
# print(optimized_factorial(12))     # 1