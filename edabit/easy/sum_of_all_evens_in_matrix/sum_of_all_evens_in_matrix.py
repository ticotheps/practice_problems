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