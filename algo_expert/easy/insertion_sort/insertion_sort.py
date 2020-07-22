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
    # print(f"\narray = {array}")
    
    sorted_list = []
    # print(f"***INITIAL*** sorted_list = {sorted_list}")
    
    popped_first = array.pop(0)
    # print(f"popped_first = {popped_first}")
    
    sorted_list.append(popped_first)
    # print(f"***ADD FIRST ELEMENT*** sorted_list = {sorted_list}")
    # print(f"***UPDATED*** array = {array}")
    
    while len(array) > 0:
        # print(f"\nsorted_list[-1] = {sorted_list[-1]}")
        # print(f"array[0] = {array[0]}")
        
        if sorted_list[-1] > array[0]:
            
            last_sorted = sorted_list.pop(-1)
            # print(f"last_sorted = {last_sorted}")
            
            first_unsorted = array.pop(0)
            # print(f"first_unsorted = {first_unsorted}")
            
            sorted_list.append(first_unsorted)
            # print(f"***SWAP*** sorted_list = {sorted_list}")
            
            array.insert(0, last_sorted)
            # print(f"***SWAP*** array = {array}")
            
        if sorted_list[-1] <= array[0]:
            
            first_unsorted = array.pop(0)
            # print(f"first_unsorted = {first_unsorted}")
            
            sorted_list.append(first_unsorted)
            # print(f"***ADD TO SORTED*** sorted_list = {sorted_list}")
            
            for i in range(len(sorted_list)-1, 0, -1):
                # print(f"\nsorted_list[{i}] = {sorted_list[i]}")
                # print(f"sorted_list[{i-1}] = {sorted_list[i-1]}")
                
                if sorted_list[i] < sorted_list[i-1]:
                    new_b = sorted_list[i-1]
                    new_a = sorted_list[i]
                    sorted_list[i] = new_b
                    sorted_list[i-1] = new_a
                    # print(f"***UPDATED*** sorted_list[{i}] = {sorted_list[i]}")
                    # print(f"***UPDATED*** sorted_list[{i-1}] = {sorted_list[i-1]}")
                    
    return sorted_list

# print(insertionSort([8, 5, 2, 9, 5, 6, 3]))  # [2, 3, 5, 5, 6, 8, 9]

"""
****** REFLECT/REFACTOR ******
"""