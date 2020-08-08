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
    if len(str(n)) % 2 != 0:
        return "The provided ticket number has an odd number of digits. Please provide a valid ticket number with an even number of digits."
    n_str = str(n)
    n_str_lst = [x for x in n_str]
    half_n_len = len(n_str_lst) // 2
    half_1_lst = n_str_lst[:(half_n_len)]
    half_2_lst = n_str_lst[(half_n_len):]
    half_1_sum = 0
    half_2_sum = 0
    for char1 in half_1_lst:
        char1_int = int(char1)
        half_1_sum += char1_int
    for char2 in half_2_lst:
        char2_int = int(char2)
        half_2_sum += char2_int
    if half_1_sum == half_2_sum:
        return True
    return False