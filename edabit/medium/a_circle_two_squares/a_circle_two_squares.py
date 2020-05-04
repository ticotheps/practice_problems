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