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
"""
DEVISING A PLAN:
    (1) Create a function that takes in 1 input (an integer, "num") and returns
    1 output (a string; either: "Fizz" || "Buzz" || "FizzBuzz" || "<num>").
    
    (2) Initialize a variable, "multipleOf3", with a value of false, to indicate whether or not the input is a multiple of 3.
    
    (3) Initialize a variable, "multipleOf5", with a value of false, to indicate whether or not the input is a multiple of 5.
    
    (4) Use an "if" statement and the modulo operator to determine if the input,
    "num", is a multiple of 3. If it is a multiple of 3, set the value of "multipleOf3" to the value of True. If it is not a multiple of 3, do nothing.
    
    (5) Use an "if" statement and the modulo operator to determine if the input,
    "num", is a multiple of 5. If it is a multiple of 5, set the value of "multipleOf5" to the value of True. If it is not a multiple of 5, do nothing.
    
    (6) Use another series of "if" statements, combined with the boolean values of the "multipleOf3" and "multipleOf5" variables, to determine what to return as the output:
        (a) a multiple of 3? -> return "Fizz"
        (b) a multiple of 5? -> return "Buzz"
        (c) a multiple of both, 3 & 5 -> return "FizzBuzz"
        (d) not a multiple of either 3 or 5. -> return the string version of "num"
"""

def fizz_buzz(num):
    multipleOf3 = False
    multipleOf5 = False
    
    if num % 3 == 0:
        multipleOf3 = True
        
    if num % 5 == 0:
        multipleOf5 = True
        
    if multipleOf3 == True and multipleOf5 == True:
        return "FizzBuzz"
    elif multipleOf3 == True and multipleOf5 == False:
        return "Fizz"
    elif multipleOf3 == False and multipleOf5 == True:
        return "Buzz"
    else:
        return f"{num}"

print(fizz_buzz(3))  # Should print "Fizz"
print(fizz_buzz(5))  # Should print "Buzz"
print(fizz_buzz(15))  # Should print "FizzBuzz"
print(fizz_buzz(4))  # Should print "4"