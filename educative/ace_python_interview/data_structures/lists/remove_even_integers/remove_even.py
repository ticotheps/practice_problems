"""
REMOVE EVEN INTEGERS FROM LIST

Implement a function that removes all the even elements from a given list. Name
it "remove_even(list)".

Input:
    - A list with random integers.

Output:
    - A list with only odd integers.
    
Sample Input:
    - my_list = [1, 2, 4, 5, 10, 6, 3]
    
Sample Output:
    - my_list = [1, 5, 3]
"""

"""
U.P.E.R. Problem-Solving Framework

UNDERSTAND:
    - Objective:
        - Write an algorithm that takes in a single input list of random integers
        and returns a single output list of only odd integers.
        
    - Expected Inputs:
        - 1
        - 'list' data type
        - "list"
        
    - Expected Outputs:
        - 1
        - 'list' data type
        - "odd_list"
        
    - Constraints & Edge Cases:
        - Can the input list contain negative numbers?
            - Yes. Negative numbers are acceptable.
        - Can the input list contain floating point numbers?
            - No.
        - Can the input list be empty?
            - No. It must contain at least 1 element.
        - What happens if we're given a list and that list contains all even numbers?
            - Return an empty list.
            
PLAN:
    - Brute Force Solution:
        (1) Create a new empty list where we can store only the odd integers that
        we'll encounter while iterating through the given input list.
        
        (2) Iterate through the given input list.
        
        (3) Convert the element's value into it's absolute value in order to produce a
        positive integer, which is required for use with the modulo operator.
        
        (4) Check to see if the absolute value of the iterated-on element can be
        evenly divided by 2 (using the modulo operator):
        
            (a) If it can be, add the original iterated-on element to the new empty list
            that was created in first step.
            
            (b) If it can't be, do nothing.
            
        (5) Return the list that was created in the first step.
"""

# EXECUTE

# def remove_even(list):
#     odd_list = []                   # O(1)
    
#     for i in list:                  # O(n)
#         abs_value = abs(i)          # O(1)
        
#         if abs_value % 2 != 0:      # O(1)
#             odd_list.append(i)      # O(1)

#     return odd_list

# remove_even([1, 2, 4, 5, 10, 6, 3])


"""
REFLECT/REFACTOR:
    - Brute Force Solution:
        - Time Complexity: O(n) -> "linear time"
        - Space Complexity: O(1) -> "constant space"
    - Can this Brute Force Solution be optimized?
        - Nope!
    - Alternate solutions?
        - Yes! We can do the same thing with a list comprehension!
"""

# Alternate-more-elegant solution
def remove_even(list):
    return [x for x in list if x % 2 != 0]

remove_even([1, 2, 4, 5, 10, 6, 3])     # 1, 5, 3