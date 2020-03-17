"""
Repeating Letters
    - Objective: Create a function that takes in an input [of string data type]
    and returns an output [of string data type] in which each item in the string
    is repeated ONCE.
    
    - Examples:
        - double_char("String") ➞ "SSttrriinngg"
        - double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
        - double_char("1234!_ ") ➞ "11223344!!__  "
        
    - Constraints:
        - All test cases contain valid strings. 
        - Don't worry about spaces, special characters or numbers. 
            - They're all considered valid characters.
"""

def double_char(txt):
    # Checks for a valid input of string data.
    if type(txt) == str:
        # Create a var 'newDoubleCharsList' that is set equal to an empty list.
        newDoubleCharsList = []
        print(f"newDoubleCharsList = {newDoubleCharsList}")
        
        # Create a var 'txtCharsList' that converts input into a list of chars.
        txtCharsList = list(txt)
        print(f"txtCharsList = {txtCharsList}")
        
        return "We have a valid input"
    else:
        return "Please enter a valid input of 'str'' data type"

    

    
    # Use a 'for' loop to iterate through each char in 'textCharsList'...
        # Create a var 'newDoubleChar' that is set equal to the iterated char x2.
        # Append 'newDoubleChar' to the value of 'newDoubleCharsList'
        
    # Create a var 'newDoubleCharsStr' that is set equal to the string that
    # results when all of the items in the 'newDoubleCharsList' are joined
    # together.
    
    # Return the value of 'newDoubleCharsStr'
    
print(double_char("String"))  # should print "SSttrriinngg"
    
    