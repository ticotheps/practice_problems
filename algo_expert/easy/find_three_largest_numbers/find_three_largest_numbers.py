"""
FIND THREE LARGEST NUMBERS

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
UNDERSTAND PHASE

Objective:
    - Write an algorithm that takes in a [Python] list of integers and returns a
        list of the three largest numbers from the input array, in ascending order.
        
Expected Inputs & Outputs:
    - Inputs:
        - Number: 1
        - Data Type: list
        - Variable Name: 'input_array'
        
    - Outputs:
        - Number: 1
        - Data Type: list
        - Variable Name: 'largest_three_nums_array'
        
Constraints:
    - Can the input include negative integers?
        - Yes.
    - Can the input include floating point numbers?
        - No.
    - Can the input be empty?
        - No.
"""

# PLAN PHASE & EXECUTE PHASE

def find_three_largest_numbers(input_array):
    # Declare a var that will store the current three largest values from the 
    #   input list, in ascending order.
    largest_three_nums_array = []
    print(f"INITIAL largest_three_nums_array = {largest_three_nums_array}")
    
    # Use a 'for' loop to iterate through the 'input_array'.
    for num1 in input_array:
        print(f"num1 = {num1}")
        
        if len(largest_three_nums_array) >= 3:
            # Return the value of the 'largest_three_nums_array'.
            return largest_three_nums_array
        elif len(largest_three_nums_array) < 3 and len(largest_three_nums_array) > 0:
            for num2 in largest_three_nums_array:
                print(f"---num2 = {num2}")
        else:
            # Append 'num1' value to 'largest_three_nums_array'.
            largest_three_nums_array.append(num1)
            print(f"UPDATED largest_three_nums_array = {largest_three_nums_array}")
            
            
    
    # Return the value of the 'largest_three_nums_array'.
    return largest_three_nums_array

print(find_three_largest_numbers([0, 5, 1, 4, 2, 3]))
# print(find_three_largest_numbers([20, 39, 2, 412, 32, 232]))
# print(find_three_largest_numbers([0, -5, 1, 14, 22, -3]))