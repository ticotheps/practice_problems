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
    - The values of sequence will be between -10^5(-1,000,000; inclusive) and 10^5(1,000,000;
    inclusive).
"""