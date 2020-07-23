"""
ADVANCED LIST SORT

Create a function that takes a list of numbers or strings and returns a list
with the items from the original list stored into sublists. Items of the the
same value should be in the same sublist.

- Examples:
    - advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
    - advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
    - advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
    
- Notes:
    - The sublists should be returned in the order of each element's first
      appearance in the given list.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in a single list of either all numbers or all
      strings and returns a list of multiple sublists where each sublist only
      contains elements that are duplicates of one another.
      
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "lst"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "list_of_sublists"
    
- Edge Cases & Constraints
    - Can the given input list include a list of numbers mixed in with strings?
        - No. They must be all of one type or the other. 
    - Can the given input list include negative numbers?
        - Yes.
    - Can the given input list include floating point numbers?
        - Yes.

****** PLAN ******
- First Pass Solution:
    (1) Define a function, "advanced_sort()", that takes in 1 input list and
    returns 1 output list.

    (2) Declare a var, "elements_dict", and initialize it with an empty
    dictionary.
    
    (3) Declare a var, "list_of_sublists", and initialize it with an empty list.
    
    (4) Use a 'for' loop to iterate through the given input list...

        (a) If the iterated-on element is NOT already a key in the 
        "elements_dict" dictionary add it as a new entry and set its value 
        equal to 1 (integer data type) in order to represent the total current
        number of occurrences in the given input list.
        
        (b) If the iterated-on element IS already a key in the "elements_dict" 
        dictionary, increase the value of the matching key by 1.
            
    (5) Use another 'for' loop to iterate through the give input list...
    
        (a) Declare a var, "occurrences", and initialize it with the value for 
        the iterated-on element's matching key in the "elements_dict" 
        dictionary.
        
        (b) Declare another var, "sublist", and initialize it with a list comprehension that appends 'n' number of copies of the iterated-on element into "sublist".
        
        (c) Append "sublist" to the "list_of_sublists" list.
        
    (6) Return the value of "list_of_sublists".

****** EXECUTE ****** (Please see below)
"""

def advanced_sort(lst):
    pass

print(advanced_sort([2, 1, 2, 1]))  # [[2, 2], [1, 1]]