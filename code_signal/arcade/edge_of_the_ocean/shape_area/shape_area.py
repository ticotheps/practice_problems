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

****** EXECUTE phase ******

****** REFLECT/REFACTOR phase ******
"""

def shapeArea(n):
    pass

print(shapeArea(2))  # 5