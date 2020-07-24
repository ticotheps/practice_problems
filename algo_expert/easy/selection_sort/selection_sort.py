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
      
- Sorting Strategy:
    - Divide the unsorted input list into 2 subarrays, "sorted" and "unsorted".
    - The first element of the given input array will automatically be
    	considered the first and only element of the "sorted" subarray.
    - Iterate through the "unsorted" subarray, finding the smallest value and
    	swapping that value with the last element of the "sorted" subarray.
    - Continue iterating in this fashion until all the elements are sorted and
    	there are 0 elements left remaining in the "unsorted" subarray.

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

****** PLAN ******
- First Pass Solution:
    (1) Define a helper function, "swap()", that takes in 3 parameters,
    	"curr_index", "index_of_min", and "array", and has no outputs.
    
    (2) Define a function, "selectionSort()", that takes in an unsorted list and
    	returns a sorted version of that same list.
    
    (3) Declare a var, "curr_index", and initialize it with the value of the
    	given input's zeroith element.
    
    (4) Declare another var, "index_of_min", and initialize it with the value
    	of the given input's zeroith element.
    
    (5) Use a 'for' loop to iterate through the "unsorted" subarray by starting
    	the range() at the value of "curr_index" and ending at the value of the
    	length of the given input array minus 1.
    
        (a) If the value of the array at the iterated-on element is LESS than 
        the current value of array at the index of "index_of_min"...
        	
        	(i) call the "swap()" helper function and pass in the "curr_index",
        	the "index_of_min", and the given input "array" as arguments.
        
		(b) Increase the "curr_index" value by 1.
  
		(c) Set the value of "index_of_min" to 
        
    (6) Return the value of "array".

****** EXECUTE ****** (Please see below)

"""
# helper function
def swap(index_of_min, curr_index, array):
    array[index_of_min], array[curr_index] = array[curr_index], array[index_of_min]

def selectionSort(array):
    for i in range(0, len(array)-1):
        index_of_min = i
        smallest = array[i]
        for j in range(i+1, len(array)):
            curr_index = j
            if array[index_of_min] > array[curr_index]:
                swap(index_of_min, curr_index, array)
    return array