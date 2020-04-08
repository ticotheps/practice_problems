"""
BINARY SEARCH

Write a function that takes in a sorted array of integers, as well as a target
integer. The function should use the Binary Search Algorithm to determine if the
target integer is contained in the array and should return its index if it is,
otherwise -1.

UNDERSTAND PHASE:

Objective: 
    - Create an algorithm that takes in two inputs (an array of sorted
    integers and an integer representing a "target" value) and returns a single
    output (an integer; either the index of the target value in the array or
    -1).
    
Defining Terms:
    - "Binary Search":
        - An algorithm that can search through a sorted list of items to find a
        target value with an O(log n) run time complexity.

PLAN PHASE:

    (1) Define a function that takes in two inputs ("sortedList" & "target") and returns a single output ("matchingItemIndex" or -1). 
    
    (2) Create a variable, "matchingItemIndex", and initialize it with a value of -1.
    
    (3) Create another variable, "lenOfList", and set it equal to the length of the "sortedList" input's length.
    
    (4) Create a new variable, "minIndex", and set it equal to the zeroith index of the list.
    
    (5) Create a new variable, "maxIndex", and set it equal to the last index of the list.
    
    (6) Create a new variable, "middleIndex", and set it equal an integer that is the average of the "minIndex" and the "maxIndex" indices (rounded to the neareast whole number).
    
    (7) Use a "while" loop to continue iterating through the following block of code as long as "minIndex" is less than "maxIndex".
    
        (8) Use an "if/else" block to compare the "target" input value to the value of "sortedList" at the "middleIndex".
        
            (9) If the value of "target" is equal to the value of the "sortedList" item at the "middleIndex", then set the value of "matchingItemIndex" equal to the value of "middleIndex".
        
            (10) Else if the value of "target" is greater than the value of the "sortedList" item at "middleIndex", set "minIndex" equal to the value of "middleIndex" and find a new "middleIndex" value using the new "minIndex" value and the previous "maxIndex" value.
            
            (11) Else if the value of "target" is less than the value of the "sortedList" item at "middleIndex", set "maxIndex" equal to the value of "middleIndex" and find a new "middleIndex" value using the new "maxIndex" value and the previous "minIndex" value. 
        
    (12) Return the value of the "matchingItemIndex".
"""
# EXECUTE PHASE:

def binarySearch(sortedList, target):
    matchingItemIndex = -1
    lenOfList = len(sortedList)
    minIndex = 0
    maxIndex = lenOfList - 1
    while minIndex <= maxIndex:
        middleIndex = (minIndex + maxIndex + 1) // 2
        if target == sortedList[middleIndex]:
            matchingItemIndex = middleIndex
            return matchingItemIndex
        elif target > sortedList[middleIndex]:
            minIndex = middleIndex + 1
        else:
            maxIndex = middleIndex - 1
    return matchingItemIndex

# my_sortedList_1 = [1, 3, 5, 7, 9, 11]
# print(binarySearch(my_sortedList_1, 3))  # should return 1

# my_sortedList_2 = [1, 3, 5, 7, 9, 11]
# print(binarySearch(my_sortedList_2, 4))  # should return -1

# my_sortedList_3 = [1, 3, 5, 7, 9, 11]
# print(binarySearch(my_sortedList_3, 7))  # should return 3


"""
REFLECT/REFACTOR PHASE:
    - Runtime Complexity: O(log n)
    - Space Complexity: O(1)
"""