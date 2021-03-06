"""
ADD TWO STRING NUMBERS

Write a function that adds two numbers. The catch, however, is that the numbers
will be strings.

Examples:
    - add_str_nums("4", "5") -> "9"
    - add_str_nums("abcdefg", "3") -> "-1"
    - add_str_nums("1", "") -> "1"
    - add_str_nums("1874682736267235927359283579235789257", "32652983572985729")
   -> "1874682736267235927391936562808774986"
   
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

- Brute Force Solution:
    (1) Define a function that takes in two string inputs, 'num1' & 'num2', and
    returns a single output string (the sum of the positive integers inside of
    the input strings).
    
    (2) Evaluate both arguments to make sure that the contents of both strings
    are, in fact, positive whole numbers.
    
        (a) If they are both positive whole numbers, proceed.
        
        (b) If they are not BOTH positive whole numbers, return the string, '-1'.
        
    (3) Convert each argument from a string data type to a number data type.
    
    (4) Declare a new var, 'sum', that adds up the values of the converted
    string arguments together.
    
    (5) Convert the 'sum' var into a string data type and set it equal to a new
    var, 'sum_str'.
    
    (6) Return the value of 'sum_str'.
    
PHASE III: EXECUTE (Please See Below)
"""

def add_str_nums(num1, num2):
    sum = 0
    if type(num1) == str and type(num2) == str:        
        if num1 != "":
            for i in num1:          
                if i.isnumeric() == False:
                    return "-1"              
            sum += int(num1)
        
        if num2 != "":  
            for j in num2:
                if j.isnumeric() == False:
                    return "-1"
            sum += int(num2)

        return str(sum)
    
    else:
        return "The provided inputs are both not of string data type. Please enter a valid input."

"""
PHASE IV: REFLECT/REFACTOR

- FIRST-PASS SOLUTION:
    - Asymptotic Analysis:
        - Time Complexity: O(n) -> "linear"
        - Space Complexity: O(1) -> "constant"
        
- Could you improve the time or space complexity of your FIRST-PASS SOLUTION?
    - No.
"""