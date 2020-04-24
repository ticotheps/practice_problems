"""
---SIMON SAYS---

Objective: 
    - Create a function that takes in two lists and returns `True` if the
        second list follows the first list by ONE element, and `False` otherwise. 
    - In other words, determine if the second list is the first list shifted 
        to the right by 1.
        
Examples:
    - simon_says([1, 2], [5, 1]))                       # Should print True
    - simon_says([1, 2], [5, 5]))                       # Should print False
    - simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])      # Should print True
    - simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))     # Should print False
    
Notes:
    - Both input lists will be of the same length and will have a minimum
        length of 2.
    - The values of the zeroith indexed element in the first list and the
        'n-1'th indexed element in the second list do NOT matter.
"""

"""
---UNDERSTAND PHASE---

- Define Unknown Terms/Concepts:
    - All terms are clear and known.
    
- Define Expected Inputs & Outputs:
    - Expected Input(s):
        - Number: 2
        - Data Types (respectively):
            (1) a Python list
            (2) a Python list
        - Possible Naming Conventions:
            (1) 'list_1'
            (2) 'list_2'
            
    - Expected Output(s):
        - Number: 1
        - Data Types (respectively):
            (1) Boolean (`True` or `False`)
        - Possible Naming Conventions:
            (1) `check_for_valid_echo`
            
- Discuss Constraints:
    - Will the two lists always be the same length?
        - Yes.
    - Can the lists be empty?
        - No. Each list will have a minimum of 2 elements.
    - Can the elements of the list NOT be numbers?
        - Yes.

"""

# ---PLAN PHASE + EXECUTE PHASE---
"""
Brute Force Approach:
    - Use a nested 'for' loop approach to gain simultaneous access to the
        elements within each list. 
    - Then, begin checking for matching values, in each list, one-by-one, 
        beginning the comparison with the zeroith-indexed element of 
        'list_1' and the first-indexed element of 'list_2', incrementing 
        the index of each list by 1 until the end of the list has been 
        reached.
"""    

def simon_says(list_1, list_2):
    # Create a variable that will signifies whether or not 'list_2' follows
    #   'list_1' by ONE element.
    check_for_valid_echo = True
    
    # Use a 'for' loop to iterate through 'list_1', starting at the zeroith-index
    for i in range(0, len(list_1)-1):
        num_1 = list_1[i]
        # print(f"\nnum_1: {num_1}")
        
        num_2 = list_2[i+1]
        # print(f"num_2: {num_2}")
            
        if num_1 != num_2:
            check_for_valid_echo = False
            # print("NOT a valid echo for one another")
            return check_for_valid_echo
            
    # print("\nThese lists WERE a valid echo of one another")
    return check_for_valid_echo
    
print(simon_says([1, 2], [5, 1]))  # Should print True
print(simon_says([1, 2], [5, 5]))  # Should print False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))  # Should print True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))  # Should print False

"""
---REFLECT & REFACTOR PHASE---

Asymptotic Analysis:
    - Time Complexity: O(n) => linear
    - Space Complexity: O(1) => constant
"""
