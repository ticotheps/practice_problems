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
    
"""