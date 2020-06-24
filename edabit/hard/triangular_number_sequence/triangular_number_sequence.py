"""
TRIANGULAR NUMBER SEQUENCE

This triangular number sequence is generated from a pattern of dots that form a
triangle. The first 5 numbers of the sequence, or dots, are:

1, 3, 6, 10, 15

This means that the first triangle has just one dot, the second one has three
dots, the third one has six dots, and so on.

Write a function that gives the number of dots, 'n', with its corresponding
triangle number of the sequence.

Examples:
    - triangle(1) -> 1
    - triangle(6) -> 21
    - triangle(215) -> 23220
"""
"""
The U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND

- Objective: 
    - Write an algorithm that takes in a single input triangle number, 'n', and
    returns a single output, 'num_of_dots' (an integer).
      
- Expected Input:
    - Data Type: integer
    - Var Name: 'n'
    
- Expected Output:
    - Data Type: integer
    - Var Name: 'num_of_dots'
    
- Edge Cases & Constraints:
    - Can the input integer be negative?
        - No.
    - Can the input be a floating point number?
        - No.
    - How would you handle an input of "None"?
        - Return a string that says, "Invalid input. Please enter a positive integer."

PHASE II: PLAN

- Brute Force Solution:
    
    (1) Define a function, 'triangle', that takes in a single input, 'n', and
    returns a single output, 'num_of_dots'.
    
    (3) Declare a var, 'num_of_dots', that will be returned as the output. This
    var will represent the total number of dots required to make an equilateral
    triangle at the given 'n' (triangle number).
    
    (4) Use a 'for' loop to iterate through a range of numbers that starts with
    1 and ends with n+1.
    
        (5) Add the value of the iterator, 'i', to the currently existing value 
        for 'num_of_dots'.
    
    (6) Return the value of 'num_of_dots'.
    
    
PHASE III: EXECUTE (Please see below)

PHASE IV: REFLECT ON/REFACTOR

- Brute Force Solution:
    - Asypmptotic Analysis:
        - Time Complexity: O(n) -> "linear"
        - Space Complexity: O(1) -> "constant"

"""

def triangle(n):
    num_of_dots = 0
        
    for i in range(1, n+1):
        num_of_dots += i
    
    return num_of_dots