"""
A CIRCLE AND TWO SQUARES

Imagine a circle and two squares: a smaller and a bigger one. For the smaller
one, the circle is a circumcircle and for the bigger one, an incircle.

Objective: 
    - Create a function that takes in an integer (radius of the circle) and returns
    the square area of the square inside the circle.add()

Examples:
    - find_area_of_inner_square(5) -> 50
    - find_area_of_inner_square(6) -> 72
    - find_area_of_inner_square(7) -> 98
    
Notes:
    - Use only positive integer parameters.
"""

"""
UNDERSTAND PHASE

Defining Terms:
    - "circumcircle": a circle that passes through each of the smaller square's
        four corners.
    - "incircle": a circle that passes through each of the larger's squares's
        four sides.
        
Expected Inputs/Outputs:
    - Inputs:
        - Number: 1
        - Data Type: integer
        - Variable Name: 'radius_of_circle'
    - Outputs:
        - Number: 1
        - Data Type: integer
        - Variable Name: 'area_of_inner_square'
        
Constraints:
    - Can the input be negative?
        - No.
    - Can the input be a floating point number?
        - No.
    - Can the input be empty?
        - No.
"""

# PLAN PHASE + EXECUTE PHASE

import math

def find_area_of_inner_square(radius_of_circle):
    side_of_outer_square = radius_of_circle * 2
    
    area_of_outer_square = side_of_outer_square ** 2
    
    side_of_inner_square = math.sqrt(side_of_outer_square ** 2 / 2)
    
    area_of_inner_square = round(side_of_inner_square ** 2)
     
    return area_of_inner_square
"""
REFLECT/REFACTOR PHASE

Asymptotic Analysis:
    - Time Complexity:
        - O(1) -> "constant"
    - Space Complexity:
        - O(1) -> "constant"
"""
