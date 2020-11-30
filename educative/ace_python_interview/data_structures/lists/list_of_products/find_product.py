"""
LIST OF PRODUCTS OF ALL ELEMENTS

Given a list, modify it so that each index stores the product of all elements in
the list except the element at the index itself.

Input:
    - A list of numbers (could be floating point or integers).
    
Output:
    - A list such that each index has a product of all the numbers in the list
    except the number stored at that index.
    
Sample Input/Output #1:
    - Input arr = [1, 2, 3, 4]
    - Output arr = [24, 12, 8, 6]
    
Sample Input/Output #2:
    - Input arr = [4, 2, 1, 5, 0]
    - Output arr = [0, 0, 0, 0, 40]
"""

"""
U.P.E.R. Problem-Solving Framework

UNDERSTAND Phase:
    - Objective: 
        - Write an algorithm that takes in a single input list (containing integers
        or floating point numbers) and returns a single output list such that each
        index contains the product of all the numbers in the list except the number
        at that index.
        
    - Inputs:
        - Expecting: 1
        - Data Type: list
        - Var Name: "lst"
        
    - Outputs:
        - Expecting: 1
        - Data Type: list
        - Var Name: "lst_of_products"
        
    - Constraints & Edge Cases:
        - Can elements in the given input list be negative numbers?
            - Yes.
        - Can elements in the given input list be floating point numbers?
            - Yes. This is clearly stated in the prompt.
        - Can the given input list be empty?
            - No. Products cannot be calculated without factors.
            
PLAN Phase:
    - Brute Force Solution:
        - Iterate through the given input list twice using nested 'for' loops.
        - The inner 'for' loop will allow us to have access to the other values while
        being able to modify the value at the index of the outer 'for' loop.
        - The modification to this value will include finding the product of all the
        other values at each index. 
        - This will produce sub-par time complexity, but will get the job done until
        it can be optimized later.
"""