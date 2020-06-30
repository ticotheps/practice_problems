"""
ADD TWO STRING NUMBERS

Write a function that adds two numbers. The catch, however, is that the numbers
will be strings.

Examples:
    - add_str_nums("4", "5") -> "9"
    - add_str_nums("abcdefg", "3") -> "-1"
    - add_str_nums("1", "") -> "1"
    - add_str_nums("1874682736267235927359283579235789257", "32652983572985729")
   -> 1874682736267235927391936562808774986
   
Notes:
    - If there are any non-numerical characters, return "-1".
    - If one option is blank, the code should still work.
    - Python supports the addiion of integers without limit, try this challenge
    without using this functionality.
    - Your function doesn't have to add negative numbers.
"""

"""
The U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND

- Objective: 
    - Write an algorithm that takes in two string inputs (each containing positive
      integers) and returns one output that is the sum of those positive
      integers.
      
- Expected Inputs:
    - Number Of: 2
    - Data Types: string, string
    - Var Names: 'num1', 'num2'
    
- Expected Outputs:
    - Number Of: 1
    - Data Type: string or integer
    - Var Name: 'sum'
    
- Edge Cases & Constraints:
    - Can the input strings be empty?
        - Yes. However, only ONE of the input strings can be empty. The other
          must contain an integer.
    - Can the input strings have negative numbers?
        - No. They must only contain positive whole numbers.
    - Can the input strings have floating point numbers?
        - No. They must only contain positive whole numbers.


PHASE II: PLAN
PHASE III: EXECUTE
PHASE IV: REFLECT/REFACTOR
"""