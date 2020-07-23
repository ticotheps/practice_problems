"""
SELECTION SORT

Write a function that takes in an array of integers and returns a sorted version
of that array. Use the Selection Sort algorithm to sort the array.

- Sample Input: [8, 5, 2, 9, 5, 6, 3]
- Sample Output: [2, 3, 5, 5, 6, 8, 9]

- Hints:
    - Divide the input array into two subarrays in place.
    - The first subarray should be sorted at all times and should start with a
      length of 0, while the second subarray should be unsorted.
    - Find the smallest (or largest) element in the unsorted subarray and insert
      it into the sorted subarray with a swap.
    - Repeat this process of finding the smallest (or largest) element in the
      unsorted subarray and inserting it in its correct position in the sorted
      subarray with a swap until the entire array is sorted.
"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework

****** UNDERSTAND ******
- Objective:
    - Write an algorithm that takes in a single unsorted list and returns the
      same list, but in sorted order using the Selection Sort algorithm.
    - This sorting mechanism occurs "in place", meaning that it does not require
      storage of any external copies of the given input list.

- Expected Input(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "array"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type(s): list
    - Var Name(s): "array"
    
- Edge Cases & Constraints:
    - Does the unsorted input list need to be sorted in-place only?
        - Yes.
    - Can the given input list include negative numbers?
        - Yes.
    - Can the given input list include floating point numbers?
        - No.

****** UNDERSTAND ******

****** UNDERSTAND ******

"""

def selectionSort(array):
    pass

print(selectionSort([8, 5, 2, 9, 5, 6, 3]),[2, 3, 5, 5, 6, 8, 9])