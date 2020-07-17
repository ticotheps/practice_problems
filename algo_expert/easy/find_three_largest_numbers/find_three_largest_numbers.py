"""
FIND THE THREE LARGEST NUMBERS

Write a function that takes in an array of integers and, without sorting the
input array, returns a sorted array of the three largest integers in the input
array.

The function should return duplicate integers if necessary; for example, it
should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample Input:
    - array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    
Sample Output: 
    - [18, 141, 541]
    
Hints:
    - Can you keep track of the three largest numbers in an array as you
        traverse the input array?
    - Following the suggestion in Hint #1, try traversing the input array and
        updating the three largest numbers if necessary by shifting them
        accordingly.
    - Optimal Space & Time Complexity: O(n) time | O(1) space - where n is the
        length of the input array.
"""

"""
***** UNDERSTAND PHASE *****

Objective:
    - Write an algorithm that takes in a list of integers and returns a
        list of the three largest numbers from the input array, in ascending order.
        
Expected Inputs & Outputs:
    - Inputs:
        - Number: 1
        - Data Type: list
        - Variable Name: 'lst'
        
    - Outputs:
        - Number: 1
        - Data Type: list
        - Variable Name: 'largest_3_lst'
        
Constraints:
    - Can the input list include negative integers?
        - Yes.
    - Can the input list include floating point numbers?
        - No.
    - Can the input list be empty?
        - No.

***** PLAN PHASE *****

***** EXECUTE PHASE ***** (Please see below)
"""
def findThreeLargestNumbers(array):
    print(f"\n{array}")
    # Declare a var, "largest_3_lst", and initialize it with an empty list.
    largest_3_lst = []
    print(f"INITIAL largest_3_lst = {largest_3_lst}")
    
    for num in array:
        print(f"num = {num}")
        
        if not len(largest_3_lst):
            print("There are no numbers in the largest_3_lst")
            largest_3_lst.append(num)
            
        # if there's only 1 number in the "largest_3_lst"...
        elif len(largest_3_lst) == 1:
            # if num is GREATER than the only number in "largest_3_lst"...
            if num > largest_3_lst[0]:
                largest_3_lst.append(num)
            # if num is LESS than the only number in "largest_3_lst"...  
            elif num < largest_3_lst[0]:
                largest_3_lst.insert(0, num)
            # if num is EQUAL to the only number in "largest_3_lst"...  
            else:
                largest_3_lst.insert(0, num)
                
        # if there's only 2 numbers in the "largest_3_lst"...
        elif len(largest_3_lst) == 2: 
            # if num is LESS than or EQUAL to the first number in "largest_3_lst"...  
            if num <= largest_3_lst[0]:
                largest_3_lst.insert(0, num)
            
            # if num is GREATER than the first number in "largest_3_lst", but
            # LESS than the second number...
            elif num > largest_3_lst[0] and num <= largest_3_lst[1]:
                largest_3_lst.insert(1, num)
                
            # if num is GREATER than the first and second numbers in 
            # "largest_3_lst"...
            elif num > largest_3_lst[0] and num > largest_3_lst[1]:
                largest_3_lst.append(num)
        
        # if there's 3 numbers in the "largest_3_lst"....     
        elif len(largest_3_lst) == 3:
            # if num is GREATER than the first number in "largest_3_lst", but
            # LESS than the second number...
            if num >= largest_3_lst[0] and num < largest_3_lst[1]:
                # remove the first number
                largest_3_lst.pop(0)
                # "num" becomes the new first number
                largest_3_lst.insert(0, num)

            # if num is GREATER than the first number in "largest_3_lst", AND
            # GREATER than the second number, but LESS than the third number...
            if largest_3_lst[1] <= num < largest_3_lst[2]:
                # remove the first number
                largest_3_lst.pop(0)
                # "num" becomes the new second number
                largest_3_lst.insert(1, num)
                
            # if num is GREATER than the first, second, AND third numbers in 
            # "largest_3_lst"...  
            if num > largest_3_lst[0] and num > largest_3_lst[1] and num > largest_3_lst[2]:
                # the second number becomes the new first number
                largest_3_lst[0] = largest_3_lst[1]
                # the third number becomes the new second number
                largest_3_lst[1] = largest_3_lst[2]
                # "num" becomes the new third number
                largest_3_lst[2] = num
                
        print(f"***UPDATED*** largest_3_lst = {largest_3_lst}")
            

    # Return the value of the 'largest_3_lst'.
    return largest_3_lst

print(findThreeLargestNumbers([0, 5, 1, 4, 2, 3]))           # [3, 4, 5]
print(findThreeLargestNumbers([20, 39, 2, 412, 32, 232]))    # [39, 232, 412]
print(findThreeLargestNumbers([0, -5, 1, 14, 22, -3]))       # [1, 14, 22]

"""
***** REFLECT/REFACTOR PHASE *****


"""