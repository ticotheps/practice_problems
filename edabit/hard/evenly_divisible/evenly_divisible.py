"""
SUM OF EVENLY DIVISIBLE NUMBERS FROM A RANGE

Create a function that takes three arguments ('a', 'b', 'c') and returns the sum
of the numbers that are evenly divisible by 'c' from the range ('a', 'b')
inclusive.

- Examples:
    - evenly_divisible(1, 10, 20) -> 0
        - (No number between 1 and 10 can be evenly divided by 20.)
    - evenly_divisible(1, 10, 2) -> 30
        - (2 + 4 + 6 + 8 + 10 = 30)
    - evenly_divisible(1, 10, 3) -> 18
        - (3 + 6 + 9 = 18)
        
- Notes:
    - Return 0 if there is no number between 'a' and 'b' that can be evenly
      divided by 'c'.
"""