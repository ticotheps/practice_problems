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
    (1) Declare a cache object, 'tri_nums_cache', and initialize it with
    key:value pairs where the keys indicate the "triangle number" (the index of
    the triangle number in the sequence) and the values indicated the number of
    total dots used to form a triangle at that triangle number. 
        - i.e.  {
                    1: 1,
                    2: 2,
                    3: 6,
                    4: 10,
                    5: 15
                }
    
    (2) Define a function, 'triangle', that takes in a single input, 'n', and
    returns a single output, 'num_of_dots'.
    
    (3) Declare a var, 'num_of_dots', that will be returned as the output. This
    var will represent the total number of dots required to make an equilateral
    triangle at the given 'n' (triangle number).
    
    (4) Declare a var, 'largest_cache_key', and set it equal to the largest key
    in the 'tri_nums_cache' object. If no keys exist, set it equal to 0.
    
    (5) Declare a var, 'tri_start_num', and set it equal to 1.
    
    (6) Compare the given input, 'n', to the 'largest_cache_key' value.
        (a) If they are equal to one another, return the value of 
        "tri_nums_cache[largest_cache_key]".
        
        (b) If 'largest_cache_key' is not 0 and 'largest_cache_key' is less 
        than 'n', set the value of 'tri_start_num' equal to the value of
        'largest_cache_key'.
    
PHASE III: EXECUTE
PHASE IV: REFLECT ON/REFACTOR
"""
