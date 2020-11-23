"""
SUM OF TWO NUMBERS (with a twist)!

Find the sum of two numbers.


Examples:
    - sum2("5125515215521515", "125261616261626") -> "5250776831783141"
    - sum2("6666666666666666666666666666", "99999999999999999999999") ➞
    "6666766666666666666666666665"
    - sum2("123456789123456789123456789", "987654321987654321987654329876543") ➞
    "987654445444443445444443453333332"
    
Notes:
    - Remember how to sum two numbers ON PAPER; it could be useful.
    - Your function must run in less than 10 seconds because Edabit has a time
    limit.
    - Each input number can have 1000 digits (characters) in it.
"""

"""
U.P.E.R.

- UNDERSTAND
    - Objective: 
        - Write an algorithm that takes in two inputs (both integers that
        are represented using the 'String' data type) and returns a single output
        (an integer that is also represented using the 'String' data type).
    
    - Expected Input(s):
        - 2 expected inputs
        - both are integers that are actually of the 'String' data type
        - "num1_str", "num2_str"
    
    - Expected Output(s):
        - 1 expected output
        - an integer that is represented by a 'String' data type
        - "sum_str"
        
    - Constraints and Edge Cases:
        - Constraint #1:
            - len(num1_str) <= 1000
        - Constraint #2:
            - len(num2_str) <= 1000
        - Can either of the given inputs be negative?
            - Yes, they can be negative because the prompt doesn't explicitly
              state that they must be positive integers.
        - Can either of the given inputs be floating point numbers?
            - Yes, they can be floating point numbers because the prompt doesn't
              explicitly state that they must be positive integers.
        - Can either of the given inputs be empty strings?
            - No, because 'None' is not a number than can be added with another number.
        
- PLAN
    - Brute Force Solution
        - Use Python's new built-in 'long' type that handles operations of very
          large integers with ease.
        - This 'long' data type can store up to 832,951 digits in a single
          number.
    
    - Steps:
        (1) Define a function that takes in 2 input strings (that are each made
        up of integers) and returns a single output string (that represents the
        sum of both input strings' numeric values).
        
        (2) Convert both input strings to the respective numeric equivalents.
        
        (3) Add those numeric equivalents together and store that value as a
        'long' data type in a new variable.
        
        (4) Return the 'string' value of the aforementioned variable that is
        storing the sum of the 'long' equivalents for both input strings.
"""

# - EXECUTE
def sum2(num1_str, num2_str):
    sum_long = 0                        # O(1)
    num1_long = int(num1_str)           # O(1)
    num2_long = int(num2_str)           # O(1)
    
    sum_long = num1_long + num2_long    # O(1)
    sum_str = str(sum_long)             # O(1)

    return sum_str

"""
- REFLECT/REFACTOR
    - What is the current time complexity of your brute force solution?
        - O(5) -> O(1) -> 'constant' time
        
    - What is the current space complexity of your brute force solution?
        - O(5) -> O(1) -> 'constant' space

    - Can you optimize the time or space complexity of your brute force
      solution?
    
"""