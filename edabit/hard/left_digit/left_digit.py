"""
MOST LEFT DIGIT

Write a function that takes a string as an argument and returns the left most
integer in the string.

- Examples:
    - left_digit("TrAdE2W1n95!") ➞ 2
    - left_digit("V3r1ta$") ➞ 3
    - left_digit("U//DertHe1nflu3nC3") ➞ 1
    - left_digit("J@v@5cR1PT") ➞ 5
    
- Notes:
    - Each string will have at least two numbers.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in a single input string and returns the
      left-most integer in that string as the single output.
      
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): string
    - Var Name(s): "str"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): integer
    - Var Name(s): "left_most_int"
    
- Edge Cases & Constraints:
    - Can the given input string be empty?
        - Yes. If the given input string is empty, return a string that says,
          "Invalid input. Please enter a string with a length greater than 0."
    - Can the numbers in the given input string be negative numbers?
        - No. They must be positive integers.
    - Can the numbers in the given input string be floating point numbers?
        - No. They must be positive integers.

****** PLAN ******
- First Pass Solution:
    (1) Define a function that takes in a single input, "str", and returns a
    single output, "left_most_int".
    
    (2) Declare a var, "left_most_int", that will be returned as the output.
    Initialize it with a value of None.
    
    (3) Declare another var, "str_list", that splits the given input string's
    characters into a list.
    
    (4) Use a 'for' loop to iterate through the "str_list" list...

        (a) Use the "isnumeric()" method to determine if the iterated-on character is a number. If the character is a number, set the value of "left_most_int" to the value of the iterated-on character.
        
        (b) If it is NOT a number, do nothing.
        
    (5) Return the value of "left_most_int".


****** EXECUTE ****** (Please see below)
"""

def left_digit(num):
    pass

print(left_digit("TrAdE2W1n95!"))   # 2
print(left_digit("V3r1ta$"))        # 3

"""
****** REFLECT/REFACTOR ******

"""