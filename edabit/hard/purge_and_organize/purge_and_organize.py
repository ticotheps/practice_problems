"""
PURGE AND ORGANIZE

Given a list of numbers, write a function that returns a list that...

1. has all duplicate elements removed.
2. is sorted from least to greatest value.

Examples:
    - unique_sort([1, 2, 4, 3]) -> [1, 2, 3, 4]
    - unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) -> [1, 2, 3, 4]
    - unique_sort([6, 7, 3, 2, 1]) -> [1, 2, 3, 6, 7]
"""
"""
U.P.E.R. PROBLEM-SOLVING FRAMEWORK

PHASE I: UNDERSTAND

- Objective:
    - Write an algorithm that takes in a single input (a list) and returns an
      output (also a list) that removes any duplicate elements from the list,
      while also sorting its values from least to greatest.
      
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): 'lst'
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): 'lst'
    
- Constraints:
    - Can the elements of the input 'lst' be negative?
        - Yes.
    - Can the elements of the input 'lst' be floating point numbers?
        - Yes.
    - Can the input 'lst' be empty?
        - Yes. We will return an empty list as the output if this is the case.
    
PHASE II: PLAN

- Brute Force Solution:
    (1) Declare a var, 'cache', that will store key/value pairs where the keys
    are the elements from the input 'lst' and the values are bools where True
    represents the key's existence within the input 'lst' and False represents
    the opposite.
    
    (2) Define a method, 'unique_sort()', that takes in a single input and
    returns a single output, as outlined in the PHASE I of U.P.E.R. (above).
    
    (3) Declare a var, 'new_lst', that will be initialized with an empty set of
    square brackets.
    
    (4) Use a 'for' loop to iterate through the given input 'lst'. 
    
        (5) If the iterated element does NOT exist within 'cache' (as a key): 
            
            (a) ...add the iterated element to 'cache' as a new key and give it
            a value of True (bool).
            
            (b) ...append the value to the 'new_lst' var.
            
        (6) If the iterated element does ALREADY exist within 'cache' (as a
        key), do nothing.
        
    (7) Declare a another var, 'sorted_new_lst', that will be initialized with
    an empty set of square brackets.
    
    (8) Declare a var, 'j', that will represent the index of the currently
    iterated-on element from 'new_lst'.
    
    (9) Use a 'while' loop to iterate through the given 'new_lst' as long as
    'j' is LESS THAN len(new_lst).
    
        (10) If there are 0 elements in 'sorted_new_lst':

            (a) ...append the iterated element to 'sorted_new_lst'.
    
        (11) If there ARE elements in 'sorted_new_lst':
            (a) ...declare a var, 'element_previous_index_checked', and initialize it
            with False (bool).
            
            (b) ...declare a var, 'element_previous_index_checked', and initialize it
            with False (bool).
        
            (c) ...declare a var, 'k', that will represent the index of the 
            currently iterated-on element from 'new_lst' and initialize it with
            0.
            
            (d) ...use a 'while' loop to iterate through the given 'sorted_new_lst' as
            long as 'k' is LESS THAN len(sorted_new_lst).
            
                (i) ...use another 'while' loop to continue comparing the 
                iterated element each subsequent value of 'sorted_new_lst' as
                long as either 'element_previous_index_checked' OR 'element_previous_index_checked' is
                FALSE.
                
                    (1) If the iterated element's value is GREATER THAN the 
                    value of sorted_new_lst[k] (the FIRST element of
                    'new_lst'):
                        (a) ...set 'element_previous_index_checked' to True.
                        
                        (b) ...add 1 to 'k'.
                            
                    (2) (ELIF:) If the iterated element's value is LESS THAN 
                    OR EQUAL TO the value of sorted_new_lst[k]:
                        (a) ...set 'element_following_index_checked' to True.
                        
                        (b) ...use .insert() to insert the iterated-on element into 'sorted_new_lst' at that index of 
                        j+k-1.
                
    (12) Return the value of 'sorted_new_lst'.
    
PHASE III: EXECUTE (PLEASE SEE BELOW)
PHASE IV: REFLECT/REFACTOR
"""

def remove_duplicates(lst):
    cache = dict()
    new_lst = []

    for i in range(0, len(lst)):
        element_i = lst[i]

        if element_i not in cache:
            cache[element_i] = True
            new_lst.append(element_i)
            
    return new_lst
            
def unique_sort(lst):
    new_lst = remove_duplicates(lst)
    sorted_new_lst = []
    
    while len(new_lst) > 0:
        smallest = int(min(new_lst))
        index_of_smallest = new_lst.index(smallest)
        next_element = new_lst.pop(index_of_smallest)
        sorted_new_lst.append(next_element)

    return sorted_new_lst