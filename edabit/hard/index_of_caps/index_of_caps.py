"""
RETURN THE INDEX OF ALL CAPITAL LETTERS

Create a function that takes in a single string as an argument and returns an
ordered list containing the indices of all capital letters in the string.

Examples:
    - index_of_caps("eDaBiT") ➞ [1, 3, 5]
    - index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
    - index_of_caps("determine") ➞ []
    - index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
    - index_of_caps("sUn") ➞ [1]
    
Notes:
    - Return an empty list if no uppercase letters are found in the string.
    - Special characters ($#A%) and numbers will be included in some test cases.
"""