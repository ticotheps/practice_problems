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
        # print(f"newDoubleCharsList = {newDoubleCharsList}")
        
        # Create a var 'txtCharsList' that converts input into a list of chars.
        txtCharsList = list(txt)
        # print(f"txtCharsList = {txtCharsList}")
        
        # Use a 'for' loop to iterate through each char in 'textCharsList'...
        for char in txtCharsList:
            # Create a var 'doubleChar' that's set equal to 'char' x2.
            doubleChar = char * 2
            # print(f"doubleChar = {doubleChar}")
            
            # Append 'newDoubleChar' to the value of 'newDoubleCharsList'
            # print(f"newDoubleCharsList = {newDoubleCharsList}")
            newDoubleCharsList.append(doubleChar)
            # print(f"newDoubleCharsList = {newDoubleCharsList}")
        
        # Create a var 'newDoubleCharsStr' that is set equal to the string that
        # results when all of the items in the 'newDoubleCharsList' are joined
        # together.
        newDoubleCharsStr = ''.join(newDoubleCharsList)
        # print(f"newDoubleCharsStr = {newDoubleCharsStr}")
        # Return the value of 'newDoubleCharsStr'
        return newDoubleCharsStr
    else:
        return "Please enter a valid input of 'str'' data type"

print(double_char("String"))  # should print "SSttrriinngg"
print(double_char("Hello World!"))  # should print "HHeelllloo  WWoorrlldd!!"
print(double_char("1234!_ ")) # should print "11223344!!__  "
    