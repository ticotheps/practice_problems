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

"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in 3 inputs (integer data types; 'a', 'b',
      'c') and returns the sum of all the numbers (within the range of 'a' to
      'b', inclusive) that are evenly divisible by 'c' as the output.

- Expected Input(s):
    - Number Of: 3
    - Data Type(s): integer, integer, integer
    - Var Name(s): 'a', 'b', 'c'
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): 'sum'
    
- Edge Cases & Constraints:
    - Can the given input integers be negative?
        - Yes. However, only inputs 'a' and 'b' can be negative.
    - Can the given input integers be floating point numbers?
        - No. They must be integers.
    - What happens when there is no number between 'a' and 'b' that can be
      evenly divisible by 'c'?
        - Return 0.

****** PLAN ******
- First Pass Solution:
    (1) Define a function that takes in 3 inputs and returns a single output.
    
    (2) Declare a var, 'sum', and initialize it with a value of 0.
    
    (3) Use a 'for' loop to iterate through a range of numbers ('a' to 'b',
    inclusive)...

        (a) If the iterated-on number, 'num', is evenly divisible by 'c', then add the value of 'num' to the value of 'sum'.
        
        (b) If the iterated-on number, 'num', is NOT evenly divisibly by 'c', then do nothing.
        
    (4) Return the value of 'sum'.

****** EXECUTE ****** (Please see below)

"""

def evenly_divisible(a, b, c):
    print(f"\na = {a}\nb = {b}\nc = {c}")
    sum = 0
    print(f"\n***INITIAL*** sum = {sum}")
    
    for num in range(a, b+1):
        print(f"num = {num}")
        
        if num % c == 0:
            print(f"{num} is evenly divisible by {c}")
            sum += num
            print(f"***UPDATED*** sum = {sum}")
        
    return sum
            

print(evenly_divisible(1, 10, 20))  # 0
print(evenly_divisible(1, 10, 2))  # 30
print(evenly_divisible(1, 10, 3))  # 18

"""
****** REFLECT/REFACTOR ******

"""

