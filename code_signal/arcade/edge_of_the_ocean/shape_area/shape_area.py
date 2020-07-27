"""
SHAPE AREA

A "1-interesting polygon" is just a square with a side length of 1. An
"n-interesting" polygon is obtained by taking the "n-1 -interesting polygon and
appending "1-interesting polygons" to its rim, side by side. You can see the
"1-", "2-", "3-", and "4-" "-interesting" polygons in the picture provided.

- Example:
    - For n = 2, the output should be shapeArea(n) = 5. 
    - For n = 3, the output should be shapeArea(n) = 13
    
- Constraints:
    - 1 <= n < 10^4
"""
"""
****** UNDERSTAND phase ******
- Objective: Write an algorithm that takes in a single integer (length of 1 side
  on the "interesting polygon") for the input and returns a single integer 
  (area of the "interesting polygon") for the output.
  
- Expected input(s): 1, "n", integer data type
- Expected output(s): 1, "area", integer data type

- Constraints:
    - "n" will always be between 1 and 10,000.

****** PLAN phase ******
- Examples:
    - n = 1; area = 1
    - n = 2; area = 5 (n^2 + (n-1)^2)
    - n = 3; area = 13 (n^2 + (n-1)^2)
    - n = 4; area = 25 (n^2 + (n-1)^2)
    
- First Pass Solution:
    (1) Define a function, "shapeArea()", that takes in the number of sides of
    an interesting polygon, "n", and returns 1 output, the area of that 
    interesting polygon.
    
    (2) Declare a var, "total_area", and initialize it with a value of 0.
    
    (3) Declare a var, "curr_polygon_side_length", and initialize it with a value of n^2.
    
    (4) Declare a var, "prev_polygon_side_length", and initialize it with a value of (n-1)^2.
    
    (5) Set the value of "total_area" equal to the sum of
    "curr_polygon_side_length" and "prev_polygon_side_length".
        
    (6) Return the value of "total_area".

****** EXECUTE phase ****** (Please see below)

****** REFLECT/REFACTOR phase ******
"""

def shapeArea(n):
    total_area = 0
    print(f"\ntotal_area = {total_area}")
        
    curr_polygon_side_length = n**2
    prev_polygon_side_length = (n-1)**2
    print(f"\ncurr_polygon_side_length = {curr_polygon_side_length}")
    print(f"\nprev_polygon_side_length = {prev_polygon_side_length}")
    
    total_area += curr_polygon_side_length + prev_polygon_side_length
    print(f"*tota_area* = {total_area}")
        
    return total_area

print(shapeArea(1))  # 1 (1^2 + 0^2 = 1)
print(shapeArea(2))  # 5 (2^2 + 1^2 = 5)
print(shapeArea(3))  # 13 (3^2 + 2^2 = 13)