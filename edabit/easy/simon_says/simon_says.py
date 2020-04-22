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


"""

"""
---PLAN PHASE---


"""

# ---EXECUTE PHASE---
def simon_says(list1, list2):
    pass

print(simon_says([1, 2], [5, 1]))  # Should print True
print(simon_says([1, 2], [5, 5]))  # Should print False
print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])  # Should print True
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))  # Should print False

"""
---REFLECT & REFACTOR PHASE---
"""
