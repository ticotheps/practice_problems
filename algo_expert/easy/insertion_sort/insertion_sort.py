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
    - Write an algorithm that takes in an unsorted list of numbers and returns
      the same list, but in sorted order, using only an "insertion sort"
      algorithm.
    
- Expected Input(s):
	- Number Of: 1
  	- Data Type(s): list
  	- Var Name(s): "array"
  
- Expected Output(s):
	- Number Of: 1
  	- Data Type(s): list
  	- Var Name(s): "sorted_list"
  
- Edge Cases & Constraints:
	- Can the given input array include negative numbers?
		- Yes.
	- Can the given input array include floating point numbers?
		- No. They must be integers.
	- Can the given input array be empty?
		- No. If it is empty, return a string that says, "Invalid input. Please
		provide an array that has at least one element."

****** PLAN ******
- First Pass Solution:
    (1) Define a function that takes in an unsorted list of integers and returns
    the same list, but in sorted order.
    
    (2) Declare a var, "sorted_list", and initialize it with an empty list.
    
    (3) Remove the first element of the given input list, "array", and append it
    to the "sorted_list" list.
    
    (4) Declare a var, "array_len", and initialize it with the length of the
    given input list, "array" (after the first element has been removed).
    
    (5) Use a "while" loop to iterate through what remains of the given input 
    "array" list so long as "array_len" is not equal to 0...
    
        (a) If the value of the last element of "sorted_list" is GREATER than the value of the first element of "array", then:

            (i) Remove the elements from their current lists and set them equal to new vars.
            
            (ii) Append the new var to their proper respective list.
		
        (b) If the value of the last element of "sorted_list" is LESS than or EQUAL to the value of the first element of "array", then:

			(i) Remove the first element of "array" and append it to the "sorted_list".
    
    (6) Return the value of "sorted_list"

****** EXECUTE ****** (Please see below)
"""

def insertionSort(array):
    sorted_list = []
    popped_first = array.pop(0)
    sorted_list.append(popped_first)
    
    while len(array) > 0:
        if sorted_list[-1] > array[0]:    
            last_sorted = sorted_list.pop(-1)
            first_unsorted = array.pop(0)
            sorted_list.append(first_unsorted)
            array.insert(0, last_sorted)
        if sorted_list[-1] <= array[0]:
            first_unsorted = array.pop(0)
            sorted_list.append(first_unsorted)
            for i in range(len(sorted_list)-1, 0, -1):
                if sorted_list[i] < sorted_list[i-1]:
                    new_b = sorted_list[i-1]
                    new_a = sorted_list[i]
                    sorted_list[i] = new_b
                    sorted_list[i-1] = new_a
    return sorted_list

"""
****** REFLECT/REFACTOR ******
- Asymptotic Analysis:
	- First Pass Solution:
		- Time Complexity: O(n^2) -> "quadratic time"
		- Space Complexity: O(n) -> "linear space"

- Can you improve upon the time or space complexity of your first pass solution?
    - Yes. You can improve upon the space complexity by doing the sorting "in
      place".

- How?
	- Optimized Solution:
        (1) Define a helper function, "swap()", that takes in 3 parameters
        ("item1", "item2", and "array") and swaps the values of item1 and item2.
 
		(2) Define a function that takes in an unsorted list of integers and returns
    	the same list, but in sorted order.
     
        (3) Create two subarrays, "sorted" & "unsorted", within the given input 
        "array" through the use of a 'for' loop.
        
        	(a) Create the "unsorted" subarray by starting the range for the 
            "for" loop at index 1. 
            	(i) This means that the 0th element in "array" is considered 
        		the first & only item in the "sorted" subarray (for the time 
				being), while all the consecutive elements after the 0th 
            	element belong to the "unsorted" subarray.
            
            (b) Declare another var, "j", inside the 'for' loop to give us
            access to the "sorted" subarray from within the "unsorted" subarray.
            
            (c) Use a 'while' loop to iterate through the "sorted" subarray 
            so long as "j" is GREATER than 0 (the end of the "sorted" subarray)
            and the value of array[j] (the last item in the "sorted" subarray) is
            LESS than the value of array[j-1] (the item previous to the last
            item in the "sorted" subarray).
            
                (i) Call the "swap()" helper function and pass in "array[j]",
                "array[j-1]", and "array" as the arguments. 
            
        (4)	Return the value of "array"
"""

def insertionSort_optimized(array):
    print(f"\n***INITIAL*** array = {array}")
    
    for i in range(1, len(array)):
        print(f"\ni = {i}")
        
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            print(f"***SWAP*** array = {array}")
            j -= 1
            print(f"j = {j}")
            
    return array

# helper function
def swap(b, a, array):
    print(f"array[j] = {array[b]}")
    print(f"array[j-1] = {array[a]}")
    
    array[b], array[a] = array[a], array[b]
    
    print(f"***UPDATED*** array[j] = {array[b]}")
    print(f"***UPDATED*** array[j-1] = {array[a]}")

print(insertionSort_optimized([8, 5, 2, 9, 5, 6, 3]))