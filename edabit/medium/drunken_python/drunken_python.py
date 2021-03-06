"""
Drunken Python

Python got drunk and built-in functions 'str()' and 'int()' are acting odd:

str(4) -> 4
str("4") -> 4
int("4") -> "4"
int(4) -> "4"

You need to create two functions to substitute 'str()' and 'int()'. A function
called 'int_to_str()' that converts integers into strings and a function called
'str_to_in()' that converts strings into integers.

Examples:
    - int_to_str(4) -> "4"
    - str_to_int("4") -> 4
    - int_to_str(29348) -> "29348"
    
Notes:
    - This is meant to illustrate the dangers of using already-existing function
    names.
    - Extra points if you can de-drunk Python.
"""

"""
PHASE I (UNDERSTAND THE PROBLEM)

Objectives:
    - Create two new algorithms that will substitute for the already built-in
    Python functions 'str()' and 'int()'. 
    - The 'int_to_str()' function will take in a single input, 'num_int',
    and will return a single output, 'num_str'.
    - The 'str_to_int()' function will take in a single input, 'num_str', and
    will return a single output, 'num_int'.
    
Expected Inputs & Outputs:
    - The 'int_to_str()' function:
        - Expected Inputs:
            - Number: 1
            - Data Type: integer
            - Var Name: 'num_int'

        - Expected Outputs:
            - Number: 1
            - Data Type: string
            - Var Name: 'num_str'

    - The 'str_to_int()' function:
        - Expected Inputs: 1
            - Number: 1
            - Data Type: string
            - Var Name: 'num_str'

        - Expected Outputs:
            - Number: 1
            - Data Type: integer
            - Var Name: 'num_int'
            
Constraints:
    - The 'int_to_str()' function:
        - Can the input be: 
            - negative?
                - Yes.
            - a floating point number?
                - No.
                - Must be a whole number.
            - empty?
                - No. 
                - Input must exist.

    - The 'str_to_int()' function:
        - Can the input be: 
            - negative?
                - Yes.
            - a floating point number?
                - No.
                - Must be a whole number.
            - empty?
                - No. 
                - Input must exist.
"""

# PHASE II (DEVISE A PLAN)
# PHASE III (EXECUTE THE PLAN)

str, int = int, str

def int_to_str(n):
	return str(n)

def str_to_int(s):
	return int(s)

"""
PHASE IV (REFLECT ON & REFACTOR THE PLAN + THE IMPLEMENTATION)

FIRST PASS SOLUTION:

    Asymptotic Analysis:
        - Time Complexity:
            - O(1) -> constant time
        - Space Complexity:
            - O(1) -> constant space
"""