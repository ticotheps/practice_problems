"""
Using list comprehensions, create a function that finds all even numbers from 1
to the given number.

Examples:
- find_even_nums(8) -> [2, 4, 6, 8]
- find_even_nums(4) -> [2, 4]
- find_even_nums(2) -> [2]
"""

def find_even_nums(n):
    even_nums_arr = [even_num for even_num in range(1,n + 1) if even_num % 2 == 0]
    return even_nums_arr