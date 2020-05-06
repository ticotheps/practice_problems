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
        - Variable Name: 'three_largest_array'
        
Constraints:
    - Can the input include negative integers?
        - Yes.
    - Can the input include floating point numbers?
        - No.
    - Can the input be empty?
        - No.
"""