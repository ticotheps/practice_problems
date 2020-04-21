"""
Sum Of All Evens In A Matrix

Objective
    - Create a function that returns the even_sum of all even numbers from a 2D
    matrix.
    
Examples
    - sum_of_evens([
        [1, 0, 2],
        [5, 5, 7],
        [9, 4, 3]
    ])  # Should print 6 (2 + 4 = 6)
        
    - sum_of_evens([
        [1, 1],
        [1, 1]
    ])  # Should print 0 (***no even numbers exist in this 2D matrix)
        
    - sum_of_evens([
        [42, 9],
        [16, 8]
    ])  # Should print 66 (42 + 16 + 8 = 66)
    
    - sum_of_evens([
        [],
        [],
        []
    ])  # Should print 0 (***no even numbers exist in this 2D matrix)
    
Notes
    - Sub-matrices will always be of equal length.
    - Return 0 if the 2D matrix only consists of empty submatrices.
"""
"""
UNDERSTAND PHASE

Defining Terms
    - "2D Matrix": A Python list that contains sub-lists, where the number of
    individual elements within each sub-list is equal to the total number of
    lists.
    
Expected Inputs & Outputs
    Inputs
        - Expected Number: 1
        - Data Type(s): a Python list (of sub-lists)
        - Name(s): 'num_matrix'
        
    Outputs
        - Expected Number: 1
        - Data Type(s): an integer
        - Name(s): 'even_sum'
        
Constraints
    - Can the input matrix contain negative values?
        - Yes.
    - Can the input matrix contain floating point numbers?
        - No.
    - Can the input matrix contain sub-lists that have different numbers of
      elements within them?
        - No. 
    - What happens if the input matrix contains a sub-list that has no elements?
        - Return 0 if the input matrix contains sub-lists with unequal lengths.
"""
"""
PLAN PHASE
    (1) Create a function that takes in a single parameter, 'num_matrix', and
        returns a single output, 'even_sum'.
        
    (2) Create a variable, 'first_sublist_len', that represent the number of
        elements within the first element of the 2D matrix.
    
    (3) Create a variable, 'even_sum', that represents the running total of 
        all even numbers within the 'num_matrix' input. Initialize this 
        'even_sum' variable with a value of 0.
    
    (4) Use a 'for' loop to iterate through each list within the 'num_matrix' input.

        (a) Create a variable, 'sublist_len', that represents the length of each
            iterated on SUBLIST from the 'num_matrix' input list. 
    
        (b) If the iterated on element's 'sublist_len' is NOT equal to the
            'first_sublist_len', returnt the current value of 'even_sum'.
            
        (c) If the iterated on element's 'sublist_len' IS equal to the
            'first_sublist_len', continue to the next code block.
            
            (5) Use a nested 'for' loop to iterate through each number in the currently iterated on sub-list.
                
                (a) If the number is EVEN, add its value to the 'even_sum' value.
                
                (b) If the number is ODD, do nothing.
                
    (6) Return the value of 'even_sum'.
"""
# EXECUTE PHASE

def sum_of_evens(num_matrix):
    first_sublist_len = len(num_matrix[0])
    print(f"\nfirst_sublist_len = {first_sublist_len}")
    
    even_sum = 0
    print(f"INITIAL even_sum = {even_sum}\n")
    
    for sublist in num_matrix:
        if len(sublist) != first_sublist_len:
            return even_sum
        else:
            for num in sublist:
                if num != 0 and num % 2 == 0:
                    print("\nEVEN NUMBER FOUND!")
                    print(f"num = {num}")
                    even_sum += num
                    print(f"CHANGED even_sum = {even_sum}\n")
                
    return even_sum
"""
REFLECT/REFACTOR PHASE

Asymptotic Analysis

    - THE BRUTE FORCE SOLUTION
        - Run Time Complexity: O(n^2) = "quadratic"
        - Space Complexity: O(1) = "constant"
"""