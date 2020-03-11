"""
List of Multiples
    - Objective: Create a function that takes two numbers as arguments (num, length) and returns
    a list of multiples of num up to length.
    
    - Examples:
        - get_list_of_multiples(7, 5) -> [7, 14, 21, 28, 35]
        - get_list_of_multiples(12, 10) -> [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
        - get_list_of_multiples(17, 6) -> [17, 34, 51, 68, 85, 102]
        
    - Hints:
        - Note that our argument 'num' is also included in the returned list.
"""
"""
UNDERSTANDING THE PROBLEM:
    - Objective: Create an algorithm that takes in 2 inputs ("num", "length")
    and returns 1 output, "multiples_list", containing "length" number of
    multiples in the list (one of which includes the "num" itself).
    
    - Expected Inputs/Outputs:
        - Inputs: 2
            - "num" (data type: integer)
            - "length" (data type: integer)
        - Outputs: 1
            - "multiples_list" (data type: python list)
            
    - Constraints:
        - "num" must be an positive, whole integer.
        - "length" must be an positive, whole integer.
        - "num" & "length" cannot be negative numbers.
        - "num" & "length" cannot be floating point numbers.
        
    - Hints:
        - Note that the "num" argument will always be the first item in the returned list.
"""
"""
DEVISING A PLAN:
    (1) Create a function that takes in 2 inputs ("num", "length")
    and returns 1 output, "multiples_list".
    
    (2) Initialize a new "multiples_list" variable with an empty array to store the list of multiples that we would like to return.
    
    (3) Use a 'for' loop to iterate through a range of numbers where the start value is 1 and the end value is "length" + 1 (to account for the 'range()' method starting at 1 instead of at 0).
    
    (4) Inside the 'for' loop, multiply 'multiple_of_num' by "num" and set that new value equal to 'multiple_of_num'.
    
    (5) Inside the 'for' loop, declare a new "multiple_of_num" variable and set it equal to the value of "num" multiplied by "i" (the iterator).
    
    (6) While still inside the 'for' loop, append the new value of 'multiple_of_num' to the 'multiples_list'.
    
    (7) After the 'for' loop finishes executing, return the value of 'multiples_of_num'.
"""
# EXECUTE:

def get_list_of_multiples (num, length):
    multiples_list = []
    
    for i in range(1, length + 1):
        multiple_of_num = num * i
        multiples_list.append(multiple_of_num)
    return multiples_list

"""
REFLECTION/REVIEW:
    - Asymptotic Analysis:
        - Runtime Complexity: O(n) -> linear runtime
        - Space Complexity: O(2) -> O(1) -> constant space
    
    - Can we optimize the runtime complexity for this?
        - Yes. You could always use memoization with a 'cache' object to
        store previously calculated lists of multiples, where in the key/value
        pair, the 'key' was the "num" variable and the associated multiples list
        was the value.
"""