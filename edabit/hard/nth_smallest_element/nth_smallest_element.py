"""
NTH SMALLEST ELEMENT

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the FIRST smallest, the second smallest element is the
second smallest, etc.).

Examples:
    - nth_smallest([1, 3, 5, 7], 1) -> 1
    - nth_smallest([1, 3, 5, 7], 3) -> 5
    - nth_smallest([1, 3, 5, 7], 5) -> None
    - nth_smallest([7, 3, 5, 1], 2) -> 3

Notes:
    - 'n' will always be >= 1.
    - Each number in the array will be distinct (there will be a clear
    ordering).
    - Given an out of bounds parameter (e.g. a list is of size 'k'), and you are
    asked to find the m < k smallest element, return None.
"""