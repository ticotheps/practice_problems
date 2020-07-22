"""
INSERTION SORT

Write a function that takes in an array of integers and returns a sorted version
of that array. Use the insertion sort algorithm to sort the array.

- Sample Input: [8, 5, 2, 9, 5, 6, 3]
- Sample Output: [2, 3, 5, 5, 6, 8, 9] 

- Hints:
    - Divide the input array into two subarrays in place.
    - The first subarray should be sorted at all times and should start with a
      length of 1.
    - The second subarray should be unsorted.
    - Iterate through the unsorted subarray, inserting all of its elements into
      the sorted subarray in the correct position by swapping them into place.
    - Eventually, the entire array will be sorted.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
  - Write an algorithm that takes in an unsorted list of numbers and returns the
    same list, but in sorted order, using only an "insertion sort" algorithm.
    
- Expected Input(s):
  - Number Of: 1
  - Data Type(s): list
  - Var Name(s): "array"
  
- Expected Output(s):
  - Number Of: 1
  - Data Type(s): list
  - Var Name(s): "array"
  
- Edge Cases & Constraints:
  - Can the given input array include negative numbers?
    - Yes.
  - Can the given input array include floating point numbers?
    - No. They must be integers.
  - Can the given input array be empty?
    - No. If it is empty, return a string that says, "Invalid input. Please
      provide an array that has at least one element."

****** UNDERSTAND ******


****** UNDERSTAND ******

"""

def insertionSort(array):
    pass

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))  # [2, 3, 5, 5, 6, 8, 9]