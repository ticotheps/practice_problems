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
- First Pass Solution:
    (1) Define a function that takes in an unsorted list, "array", and returns
    the same list, but with all of the elements of that list sorted in ascending
    order.
    
    (2) Declare a var, "swap_occurred", and initialize it with a Boolean value
    of True.
    
    (3) Use a 'while' loop to iterate through the given input "array" list,
    while "swap_occurred" is equal to True.
    
        (a) Set the Boolean value of "swap_occurred" to False.

        (b) Use a 'for' loop to iterate through the given input "array" list...
        
            (i) If "array[i]" is GREATER than "array[i+1]"...
            
                (1) Swap the values of the indices, where the value of "array[i]" now becomes the value of "array[i+1]" and vice versa.
                
                (2) Set the Boolean value of "swap_occurred" back to True.
            
            (ii) Else...
                
                (1) Do nothing.
                
    (4) Return the value of "array" after it has been sorted in ascending order.

****** EXECUTE Phase ****** (Please see below)

"""

def bubbleSort(array):
    swap_occurred = True
    while swap_occurred == True:
        swap_occurred = False
        for i in range(0, len(array)-1):
            element_a = array[i]
            element_b = array[i+1]
            
            if element_a > element_b:
                array[i] = element_b
                array[i+1] = element_a
                swap_occurred = True
    return array