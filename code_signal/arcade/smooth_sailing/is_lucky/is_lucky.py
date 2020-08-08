"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
isLucky(n) = true;
For n = 239017, the output should be
isLucky(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def isLucky(n):
    # evaluate for even number of digits.
        # if not even, return a string to ask the user to provide a valid string.

    # declare a new var, "n_str", and convert "n" to a string of integers.
        
    # declare a new var, "half_1_str", and use slicing to get the first half of
    # characters from "n_str".
    
    # declare a new var, "half_2_str", and use slicing to get the second half of
    # characters from "n_str".
    
    # declare a new var, "half_1_sum", and set it equal to 0.
    
    # declare a new var, "half_2_sum", and set it equal to 0.
    
    # use a 'for' loop to iterate through "half_1_str"...
        # convert the iterated-on element to an integer.
        # add the integer value of that iterated-on element to "half_1_sum".
        
    # use a 'for' loop to iterate through "half_2_str"...
        # convert the iterated-on element to an integer.
        # add the integer value of that iterated-on element to "half_2_sum".

    # if "half_1_sum" is equal to "half_2_sum", return True.
    # else, return False.
print(isLucky(1230))  # True
print(isLucky(239017))  # False