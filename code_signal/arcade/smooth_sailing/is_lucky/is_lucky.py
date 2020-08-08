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
    
    # evaluate for even number of digits in "n". If not even, return a string 
    # requesting the user to provide a valid string.
    if len(str(n)) % 2 != 0:
        return "The provided ticket number has an odd number of digits. Please provide a valid ticket number with an even number of digits."
    
    # declare a new var, "n_str", and convert "n" to a string of integers.
    n_str = str(n)
    print(f"\n_str = {n_str}")
    
    n_str_lst = [x for x in n_str]
    print(f"n_str_lst = {n_str_lst}")
    
    half_n_len = len(n_str_lst) // 2
    print(f"half_n_len = {half_n_len}")
    


    # declare a new var, "half_1_str", and use slicing to get the first half of
    # characters from "n_str".
    half_1_lst = n_str_lst[:(half_n_len)]
    print(f"half_1_lst = {half_1_lst}")
    
    # declare a new var, "half_2_str", and use slicing to get the second half of
    # characters from "n_str".
    half_2_lst = n_str_lst[(half_n_len):]
    print(f"half_2_lst = {half_2_lst}")
    
    # declare a new var, "half_1_sum", and set it equal to 0.
    half_1_sum = 0
    print(f"half_1_sum = {half_1_sum}")
    
    # declare a new var, "half_2_sum", and set it equal to 0.
    half_2_sum = 0
    print(f"half_2_sum = {half_2_sum}")
    
    # use a 'for' loop to iterate through "half_1_lst"...
    for char1 in half_1_lst:
        # convert the iterated-on element to an integer.
        char1_int = int(char1)
        print(f"char1_int = {char1_int}")
        
        # add the integer value of that iterated-on element to "half_1_sum".
        half_1_sum += char1_int
        print(f"*half_1_sum = {half_1_sum}")
        
    # use a 'for' loop to iterate through "half_2_lst"...
    for char2 in half_2_lst:
        # convert the iterated-on element to an integer.
        char2_int = int(char2)
        print(f"char2_int = {char2_int}")
        
        # add the integer value of that iterated-on element to "half_2_sum".
        half_2_sum += char2_int
        print(f"*half_2_sum = {half_2_sum}")

    # if "half_1_sum" is equal to "half_2_sum", return True.
    # else, return False.
    if half_1_sum == half_2_sum:
        return True
    return False


print(isLucky(1230))  # True
print(isLucky(239017))  # False