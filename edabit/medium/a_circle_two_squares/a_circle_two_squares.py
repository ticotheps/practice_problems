"""
A CIRCLE AND TWO SQUARES

Imagine a circle and two squares: a smaller and a bigger one. For the smaller
one, the circle is a circumcircle and for the bigger one, an incircle.

Objective: 
    - Create a function that takes in an integer (radius of the circle) and returns
    the square area of the square inside the circle.add()

Examples:
    - square_areas_difference(5) -> 50
    - square_areas_difference(6) -> 72
    - square_areas_difference(7) -> 98
    
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

def square_areas_difference(radius_of_circle):
    
    # Declare a variable to store the length of one side of the outer square
    #   in relation to the given input.
    side_of_outer_square = radius_of_circle * 2
    print(f"side_of_outer_square = {side_of_outer_square}")
    
    # Declare a variable to store the area of the outer square
    area_of_outer_square = side_of_outer_square ** 2
    print(f"area_of_outer_square = {area_of_outer_square}")
    
    # Declare a variable to store the length of one side of the inner square
    side_of_inner_square = math.sqrt(side_of_outer_square ** 2 / 2)
    print(f"side_of_inner_square = {side_of_inner_square}")
    
    # Declare a variable to store the area of the inner square to be returned
    #   and make sure that it is rounded to the nearest integer.
    area_of_inner_square = round(side_of_inner_square ** 2)
     
    return area_of_inner_square

print(square_areas_difference(5))  # 50
print(square_areas_difference(6))  # 72
print(square_areas_difference(7))  # 98