"""
****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in an integer, "n", and an array (of integers), "a", and returns a 
    single mutated array that follows the given rules:
        - For each index of "b" (to-be-returned mutated array) = a[i-1] + a[i] + a[i+1]
        - If a specific index does not exist, set the value equal to 0.

****** PLAN ******
- First Pass Solution:
    (1) Define a function, "mutateTheArray()", that takes in 2 inputs, "n" and "a", and returns 1 output,
    "b".
    
    (2) Declare a var, "b", and initialize it with an empty array.
    
    (3) Use a 'for' loop to iterate through a range of numbers, starting with 0 (inclusive) and ending with
    "n-1" (exclusive), where the iterator is "i".
    
        (a) Define 3 new vars: "a_index_minus_1", "a_index", & "a_index_plus_1" and initialize it with a
        value of 0.
        
        (b) Use an "if" statement to evaluate how to set a value for each of the above vars.
            
            (i) If a value exists at the given index for the var, set the associated var's value to the 
            existing value from array "a".

            (ii) If the value does NOT exist at the given index for the var, set the associated var equal 
            to a value of 0.        

        (c) Set the value of a new var, "b_element", to be the sum total of all three above vars.
        
    (4) Return the value of "b".

****** EXECUTE ****** (Please see below)
"""

def mutateTheArray(n, a):
    # print(f"a = {a}")
    b = []
    # print(f"b = {b}")
    
    for i in range(0, len(a)):
        # print(f"\ni = {i}")
        element_1 = 0
        # print(f"element_1 = {element_1}")
        element_2 = 0
        # print(f"element_2 = {element_2}")
        element_3 = 0
        # print(f"element_3 = {element_3}")
        
        if i-1 < 0:
            element_2 = a[i]
            # print(f"***UPDATED*** element_2 = {element_2}")
            element_3 = a[i+1]
            # print(f"***UPDATED*** element_3 = {element_3}")
            
        if 1 <= i < len(a)-1:
            element_1 = a[i-1]
            # print(f"***UPDATED*** element_1 = {element_1}")
            element_2 = a[i]
            # print(f"***UPDATED*** element_2 = {element_2}")
            element_3 = a[i+1]
            # print(f"***UPDATED*** element_3 = {element_3}")
            
        if i+1 >= len(a):
            element_1 = a[i-1]
            # print(f"***UPDATED*** element_1 = {element_1}")
            element_2 = a[i]
            # print(f"***UPDATED*** element_2 = {element_2}")
            
        b_element = element_1 + element_2 + element_3
        # print(f"b_element = {element_1} + {element_2} + {element_3}")
        b.append(b_element)
        # print(f"***UPDATED*** b = {b}")

    return b
            
print(mutateTheArray(5, [4, 0, 1, -2, 3]))  # [4, 5, -1, 2, 1]

"""
****** REFLECT/REFACTOR ******
- Asymptotic Analysis:
    - First Pass Solution:
        - Time Complexity: O(n) -> "linear time"
        - Space Complexity: O(n) -> "linear space"
"""