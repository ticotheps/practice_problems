"""
BUBBLE SORT

Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Bubble Sort algorithm to sort the array.

Sample Input:
    - array = [8, 5, 2, 9, 5, 6, 3]
    
Sample Output:
    - [2, 3, 5, 5, 6, 8, 9]
    
Notes:
    - "Bubble Sort" is different from other sorting algorithms because it sorts
    "in place", meaning that it does not return a new array.
    - It returns the original, but in a sorted order.
"""
"""
****** UNDERSTAND Phase ******
- Objective:
    - Write an algorithm that uses "Bubble Sort" to sort the integers in a given
    input list and returns the sorted version of that input list.
    
- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "array"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "array"
    
- Hints:
    - Traverse the input array, swapping any two numbers that are out of order.
    - Keep track of any swaps that you make during an iteration.
    - Once you arrive at the end of the array, check if you have made any swaps.
    - If not, the array is sorted and you are done!
    - Otherwise, repeat the steps laid out in this hint until the array is sorted.

****** PLAN Phase ******


****** EXECUTE Phase ******

"""

def bubbleSort(array):
    pass

print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))  # [2, 3, 5, 5, 6, 8, 9]