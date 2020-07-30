"""
ALMOST INCREASING SEQUENCE

Given a sequence of integers as an array, determine whether it is possible to
obtain a strictly increasing sequence by removing no more than one element from
the array.

Notes: 
    - Sequence a(0), a(1), ..., a(n) is considered to be a strictly increasing
    sequence if a(0) < a(1) < ... < a(n).
    - A sequence only containing one element is also considered to be strictly
    increasing.

Examples:
    - For sequence = [1, 3, 2, 1], the output should be:
        - almostIncreasingSequence(sequence) = False
        - There is no one element in this array that can be removed in order to get
        a strictly increasing sequence.
    - For sequence = [1, 3, 2], the output should be:
        - almostIncreasingSequence(sequence) = True
        - You can remove "3" from the array to get the strictly increasing sequence
        [1, 2].
        - Alternately, you can remove "2" to get the strictly increasing sequence
        [1, 3].
        
Constraints:
    - The length of sequence will be between 2(inclusive) and 10^5(1,000,000;
    inclusive).
    - The values of the sequence will be between -10^5(-1,000,000; inclusive) and 10^5(1,000,000;
    inclusive).
"""

"""
****** UNDERSTAND Phase ******
- Objective: Write an algorithm that takes in a single input list, evaluates
  whether or not a single element could be removed from the list to make its order
  "strictly increasing", and then returns True or False (Boolean value) depending on
  whether or not it can do that.
  
- Expected Input(s): 1; list data type; "sequence"
- Expected Output(s): 1; Boolean data type; True or False

- Edge Cases & Constraints:
    - The length of any given input list will be between 2 and 1000000.
    - The value of any element in any given input list will be between -1000000
      and 1000000.
      
      
****** PLAN Phase ******
- First Pass Solution:
    (1) Define a helper function, "isStrictlyIncreasing(lst)", that takes in a list
    and returns True or False based on whether or not the given input list is in
    'strictly increasing' order.
    
    (2) Define a function, "almostIncreasingSequence(sequence)", that takes in a list,
    determines whether or not a single element can be removed from the list to
    put the remaining elements in 'strictly increasing" order, and returns True
    or False based on whether or not it can do this.
    
        (a) Define a var, "verified_strictly_increasing", and initialize it with a
        value of False (Boolean value).
    
        (b) Use a 'for' loop to iterate through a range of numbers, beginning with 
        0 (inclusive) and ending with the length of the given input list...

            (i) Declare a var, "test_list", that will be a replica of the given input
            list.
            
            (ii) Remove the value of "test_list" at the index of iterator "i".
            
            (iii) Use the helper function, "isStrictlyIncreasing()", to determine
            if the remaining elements in "test_list" are in strictly increasing order.
            
            (iv) If they are in strictly increasing order, set the value of
            "verified_strictly_increasing" to True and return that value.
            
            (v) If they are NOT in strictly increasing order, do nothing.
        
        (c) Return the value of "verified_strictly_increasing".
"""
