"""
FizzBuzz Interview Question

Create a function that takes a number as an argument and returns "Fizz", "Buzz"
or "FizzBuzz".

Constraints:
    - If the number is a multiple of 3 the output should be "Fizz".
    - If the number given is a multiple of 5, the output should be "Buzz".
    - If the number given is a multiple of both 3 and 5, the output should be
    "FizzBuzz".
    - If the number is not a multiple of either 3 or 5, the number should be
    output on its own as shown in the examples below.
    
Examples:
    - fizz_buzz(3) => "Fizz"
    - fizz_buzz(5) => "Buzz"
    - fizz_buzz(15) => "FizzBuzz"
    - fizz_buzz(4) => "4"
    
Hints:
    - Try to be precise with how you spell things and where you put the capital
    letters.
"""
"""
UNDERSTANDING THE PROBLEM:
    - Objective: Create a function that takes in ONE argument (an integer;
    'num') and returns ONE output (a string; 'resultStr').
    
    - Expected Inputs/Outputs:
        - Inputs expected: 1 (integer; "num")
        - Outputs expected: 1 (string; "resultStr")
        
    - Constraints:
        - Casing and spelling matters.
        - Inputs MUST be whole integers.
        - Inputs CAN be negative numbers.
"""

def fizz_buzz(num):
    pass

print(fizz_buzz(3)) -> # Should print "Fizz"
print(fizz_buzz(5)) -> # Should print "Buzz"
print(fizz_buzz(15)) -> # Should print "FizzBuzz"
print(fizz_buzz(4)) -> # Should print "4"