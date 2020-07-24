"""
TRANSFORM INTO A LIST WITH NO DUPLICATES

A set is a collection of unique items. A set can be formed from a list from
removing all duplicate items.

Create a function that sorts a list and removes all duplicate items from it.

- Examples:
    - setify([1, 3, 3, 5, 5]) ➞        [1, 3, 5]
    - setify([4, 4, 4, 4]) ➞           [4]
    - setify([5, 7, 8, 9, 10, 15]) ➞   [5, 7, 8, 9, 10, 15]
    - setify([3, 3, 3, 2, 1]) ➞        [1, 2, 3]
"""

"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND Phase ******
- Objective:
    - Write an algorithm that takes in a single input list and then returns a
      version of that list where any duplicates have been removed and all
      elements have been sorted.
      
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "lst"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "set_lst"
    
- Edge Cases & Constraints:
    - Can the given input list include strings?
        - Yes.
    - Can the given input list be empty?
        - No. If this is the case, return a string that says, "Invalid input.
          Please provide a string with at least 1 element."
    - Can the elements in the given input list be negative numbers?
        - Yes.
    - Can the elements in the given input list be floating point numbers?
        - Yes.
    
****** PLAN Phase ******
- First Pass Solution:
    (1) Define a function that takes in 1 input, "lst", and returns 1 output,
    "set_lst".
    
    (2) Declare a var, "lst_dict", and initialize it with an empty dictionary.
    
    (3) Declare a var, "lst_set", and initialize it with an empty list.
    
    (4) Declare a var, "sorted_lst", and initialize it with a sorted version of
    the given input "lst" using the '.sorted()' method.
    
    (5) Use a 'for' loop to iterate through the "sorted_lst" where "element"
    will be the iterator...

        (a) If "element" does NOT exist in the "lst_dict" as a key, then add 
        an entry for it where "element" is the key and False (Boolean data type)
        is the value (in a key/value pair).
        
        (b) If "element" DOES already exist in the "lst_dict" as a key, do 
        nothing.
        
    (6) Use another 'for' loop to iterate through the "sorted_lst" where "item"
    will be the iterator...
    
        (a) If "item" DOES exist as a key in the "lst_dict" and the value for 
        it is False (Boolean data type), then change the value from True to
        False and append "item" to the "lst_set" list.
        
        (b) Else, do nothing.
        
    (7) Return the value of "lst_set".

****** EXECUTE Phase ****** (Please see below)
"""

def setify(lst):
    print(f"/nlst = {lst}")
    
    lst_dict = {}
    print(f"*INITIAL* lst_dict = {lst_dict}")
    
    lst_set = []
    print(f"*INITIAL* lst_set = {lst_set}")
    
    sorted_lst = sorted(lst)
    print(f"sorted_lst = {sorted_lst}")
    
    for element in sorted_lst:
        print(f"element = {element}")
        
        if element not in lst_dict:
            lst_dict[element] = False
            print(f"***UPDATED*** lst_dict = {lst_dict}")
            
        else:
            print(f"{element} already exists as a key in the 'lst_dict'!")
        
    for item in sorted_lst:
        print(f"item = {item}")
        
        if item in lst_dict and lst_dict[item] == False:
            print(f"*INITIAL* lst_dict[{item}] = {lst_dict[item]}")
            
            lst_dict[item] = True
            print(f"***UPDATED*** lst_dict[{item}] = {lst_dict[item]}")
            
            lst_set.append(item)
            print(f"***UPDATED*** lst_set = {lst_set}")
            
    return lst_set

print(setify([1, 3, 3, 5, 5, 5]))  # [1, 3, 5]