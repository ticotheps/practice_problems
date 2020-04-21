"""
Sum Of All Evens In A Matrix

Objective
    - Create a function that returns the sum of all even numbers from a 2D
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
        - Name(s): 'sum'
        
Constraints
    - Can the input matrix contain negative values?
        - Yes.
    - Can the input matrix contain floating point numbers?
        - No.
    - Can the input matrix contain sub-lists that have different numbers of
      elements within them?
        - No. 
    - What happens if the input matrix contains a sub-list that has no elements?
        - Return 0 if the number of total sub-lists is NOT equal to the number of
        elements within each sub-list.
"""
# EXECUTE PHASE


"""
REFLECT/REFACTOR PHASE

"""