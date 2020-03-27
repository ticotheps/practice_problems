"""
Card Counting ("Black Jack")

In Black Jack, cards are counted with the following values: -1, 0, 1.
    - The following cards would each be counted as +1: 
        - 2, 3, 4, 5, 6.
    - The following cards would each be counted as 0: 
        - 7, 8, 9. 
    - The following cards would each be counted as -1: 
        - 10, J, Q, K, A.
        
Objective: 
    - Create a function/algorithm that counts the number and returns it
    from the list of cards provided.
    
Understand:
    - Define Unknown Terms:
        - None.
    - Expected Inputs & Outputs:
        - Inputs:
            - Number: 1
            - Data Type: a Python list that may contain integers or strings
            - Name: 'cards_list'
        
        - Outputs:
            - Number: 1
            - Data Type: integer
            - Name: 'cards_count'
            
    - Constraints:
        - String inputs (in the input list) will always be upper case.
        - You do NOT need to consider case sensitivity.
        - If the argument is empty, return 0.
        - No items in the input list other than: 
            - 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
            
    - Examples: 
        - Example 1: count([5, 9, 10, 3, "J", "A", 4, 8, 5]) -> 1
        - Example 2: count(["A", "A", "K", "Q", "Q", "J"]) -> -6
        - Example 3: count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) -> 5
"""