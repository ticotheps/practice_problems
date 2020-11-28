"""
MERGE TWO SORTED LISTS

Objective:
    - Implement a function that merges two sorted lists, of 'm' and 'n' elements
    respectively, into another sorted list. Name it 'merge_lists(lst1, lst2)'.

Inputs:
    - Two sorted lists.
    
Outputs:
    - A merged and sorted list consisting of all elements of both input lists.
    
Sample Inputs:
    - list1 = [1, 3, 4, 5]
    - list2 = [2, 6, 7, 8]
    
Sample Output:
    - arr = [1, 2, 3, 4, 5, 6, 7, 8]
"""

"""
U.P.E.R. Problem-Solving Framework

UNDERSTAND:
    - Objective:
        - Write an algorithm that takes in two inputs (two sorted lists of integers)
        and returns an single output (a merged and sorted list of the two input
        lists).
    
    - Inputs:
        - Expecting: 2
        - Data Types: list, list
        - Variable Names: "lst_a", "lst_b"
        
    - Outputs:
        - Expecting: 1
        - Data Type: list
        - Variable Name: "merged_lst"
        
    - Constraints & Edge Cases:
        - Can either of the input lists be empty?
            - No. You cannot merge an empty list into another list.
        - Can the input lists have a differnt number of elements in each?
            - Yes.
        - Can the input lists contain negative integers as elements?
            - Yes.
        - Can the input lists contain floating point numbers as elements?
            - No. The prompt states that the input lists will contain 'integers', which are whole numbers.
    
PLAN:
    - Brute Force Solution Overview:
    (1) Write a function that takes in 2 arguments ("lst_a" and "lst_b") which
    are sorted lists and return a single output list, which is a single, merged
    & sorted list of the two given input lists.
    
    (2) Initialize two variables to represent pointers for indices of each input list as we iterate through them at different paces. The different paces of iteration are due to the dependence upon the outcome of value comparisons between the input lists when merging them together while keeping all of the elements sorted.
    
    (3) Iterate through the longer of the two input lists (with the plan of merging elements from "lst_b" INTO "lst_a") AS LONG AS "ind_a" < len(lst_a) and "ind_b" < len(lst_b):
    
        (a) Compare the value of "lst_a[ind_a]" to the value of "lst_b[ind_b]". If 'lst_a[ind_a]' < 'lst_b[ind_b]', then there will be no insert occurrence and we will just increment "ind_a" by 1.
        
        (b) If 'lst_a[ind_a]' > 'lst_b[ind_b]', we will insert 'lst_b[ind_b]' into 'lst_a' at the 'ind_a' and then we will increment both, 'ind_a' and 'ind_b', by 1.
        
    (4) If "ind_a" is equal to len(lst_a), then add the remaining (sorted) elements of 'lst_b' to the end of 'lst_a'.
    
    (5) Return 'lst_a'. 
"""

# EXECUTE phase

def merge_lists(lst_a, lst_b):
    # Init a var for current index of 'lst_a'.
    ind_a = 0
    
    # Init a var for current index of 'lst_b'.
    ind_b = 0
    
    # Iterate through the longer list of the given input lists as long as
    # 'ind_a' < len(lst_a) and 'ind_b' < len(lst_b):
    while ind_a < len(lst_a) and ind_b < len(lst_b):
        # Compare the values of each list at the current respective index as
        # indicated by the associated variables from earlier steps above.
        if lst_a[ind_a] < lst_b[ind_b]:
            ind_a += 1
        
        # If 'lst_a[ind_a]' < 'lst_b[ind_b]', then NO INSERT and increment the
        # value of 'ind_a' by 1. 
        else:
            # If 'lst_a[ind_a]' > 'lst_b[ind_b]', then INSERT the 'lst_b[ind_b]'
            # into the index of 'ind_a' and increment both values of 'ind_a' and 'ind_b'
            # by 1.
            lst_a.insert(ind_a, lst_b[ind_b])
            ind_a += 1
            ind_b += 1
        
    # If 'ind_a' == len(lst_a) and 'ind_b' < len(lst_b):
    if ind_a == len(lst_a) and ind_b < len(lst_b):
        # add the remaining elements of 'lst_b' to the end of the 'lst_a'.
        lst_a.extend(lst_b[ind_b:])
        
    # Return the value of 'lst_a'. 
    return lst_a
