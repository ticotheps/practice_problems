"""
RECURSION: FACTORIAL

Write a function that calculates the factorial of a number recursively.

Examples:
    - factorial(5) -> 120
    - factorial(3) -> 6
    - factorial(1) -> 1
    - factorial(0) -> 0
"""
"""
The U.P.E.R. Problem-Solving Framework

***** U = UNDERSTAND *****
- Objective: 
    - Write a recursive algorithm that can calculate the factorial of a given
    number.
    
- Defining Terms:
    - "Recursion": 
        - defining something with reference to itself.
            - i.e. - a function calling itself from within its own function body.
        - requirements of a recursive function:
            (a) base case
            (b) recurrence relation

- Expected Input(s):
    - Number Of: 1
    - Data Type: integer
    - Var Name: "n"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type: integer
    - Var Name: "factorial"
    
- Edge Cases & Constraints:
    - Can the given input "n" be a negative number?
        - No.
    - Can the given input "n" be a floating point number?
        - No.
    - Can the given input value be 0?
        - Yes.
        
***** P = PLAN *****
- Brute Force Solution
    (1) Define a function that takes in a single input, "n", and returns a
    single output, "factorial".
    
    (2) Use an "if" statement to define a base case. 
        (a) If "n" equals 0 or 1, return 1.
    
        (b) Else, do nothing.
    
    (3) Return the value of "n" multiplied by a recursive call to the
    find_factorial() function passing in "n-1" as the argument.
    
***** E = EXECUTE *****
***** R = REFLECT/REFACTOR *****


"""
def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * find_factorial(n-1)

print(find_factorial(0))     # 1
print(find_factorial(1))     # 1
print(find_factorial(3))     # 6
print(find_factorial(5))     # 120
    