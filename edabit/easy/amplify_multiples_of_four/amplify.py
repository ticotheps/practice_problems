"""
AMPLIFY THE MULTIPLES OF FOUR

Create a function that takes an integer and returns a list from 1 to the given
number, where:

    (1) If the number can be divided evenly by 4, amplify it by 10 (i.e. - return 10 times the number).
    
    (2) If the number cannot be divided evenly by 4, simply return the number.
    
Examples:

    (a) amplify(4) -> [1, 2, 3, 40]
    
    (b) amplify(3) -> [1, 2, 3]
    
    (c) amplify(25) -> [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
    
Notes:

    - The given integer will always be equal to or greater than 1.
        - 1 <= x < infinity

    - Include the number at the stopping point of the list.

    - To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.
"""

"""
U.P.E.R.

- UNDERSTAND
    - Objective: 
        - Write an algorithm that takes in a single input (integer) and returns
        a single output (list) where that output list contains all numbers from
        1 to the given input integer and also where any number that is evenly
        divisible by 4 is, instead, represented by that number multiplied by
        10.
        
    - Expected Inputs:
        - 1 input
        - Integer data type
        - "input_int"
        
    - Expected Outputs:
        - 1 output
        - List data type
        - "output_lst"
        
    - Personal Examples:
        - amplify(6) -> [1, 2, 3, 40, 5, 6]
        - amplify(10) -> [1, 2, 3, 40, 5, 6, 7, 80, 9, 10]
        
    - Constraints & Edge Cases:
        - Can the given input be empty?
            - No. If it was empty, we wouldn't be able to generate a list of
              numbers because we would not have an end point for the list.
        - Can the given input be negative?
            - No. The constraints clearly indicate that the given input will be
              greater than or equal to 1.
        - Can the given input be a floating point number?
            - No. The constraints of the prompt clearly indicate that the given
              input must be an integer.
- PLAN
    - Brute Force Solution:
        (1) Create an algorithm that takes in 1 input integer and returns 1
        output list.
        
        (2) Use a 'for' loop to iterate through a range of numbers, using the 1
        as the starting index and 'input_int' as the ending index (included in
        the range).
        
        (3) For any integers that are evenly divisible by 4, return that number
        multiplied by 10 instead.
        
        (4) For all other integers not evenly divisibly by 4, simply return that number.
"""
# EXECUTE

# Brute Force Solution
# def amplify(input_int):
#     output_lst = []
    
#     for i in range(1, input_int + 1): # O(n)
#         num = None # O(1)
#         if i % 4 == 0:
#             num = i * 10 # O(1)
#         else:
#             num = i # O(1)
#         output_lst.append(num) # O(1)
        
#     return output_lst

"""
- REFLECT/REFACTOR
    - Asymptotic Analysis:
        - Time Complexity:
            - O(n) -> linear
        - Space Complexity:
            - O(n) -> linear
"""

def amplify(input_int):
    return [i * 10 if i % 4 == 0 else i for i in range(1, input_int + 1)]