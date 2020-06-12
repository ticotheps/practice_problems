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
      returns a single output (integer data type), which is the factorial of the
      given input.
      
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
PHASE III: EXECUTE [the plan]
PHASE IV: REFLECT ON/REFACTOR [the plan/solution]
"""


def factorial(Z):
    print(f"\nZ = {Z}")
    
    factorial = 0
    print(f"factorial = {factorial}")
    
    return factorial

print(factorial(4))  # 24
print(factorial(0))  # 1
print(factorial(9))  # 362880
