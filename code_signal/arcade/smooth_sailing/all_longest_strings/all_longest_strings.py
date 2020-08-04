"""
UNDERSTAND Phase:

ALL LONGEST STRINGS

Given an array of strings, return another array containing all of its longest
strings.

Example:
    - Example Input: ["aba", "aa", "ad", "vcd", "aba"]
    - Example Output: ["aba", "vcd", "aba"]
"""

"""
PLAN Phase:

    (1) Declare a var, "string_lengths_cache", where the 'keys' are the unique
    lengths of strings from the given input list and the 'values' are lists of any
    strings from the given input list that have matching lengths to the 'keys'.

    (2) Declare a var, "longest_length", that will keep track of the current 
    longest string's length.
    
    (3) Use a 'for' loop to iterate through the given input list...

        (a) If the length of the iterated-on string already exists in the "string_lengths_cache"...
            (i) ...then append it to the value (of list data type).
        
        (b) If the length of the iterated-on string does NOT exist in the "string_lengths_cache", 
            (i) ...then create a new entry where the 'key' is the length of the string and the value is a list with a single element, "i", in the list.
            
            (ii) ...if the length of the iterated-on element is longer than the current value for "longest_length"...
                (1) ...then replace the current value with the length of the iterated-on element. 
                
    (4) Declare a new var, "longest_strings_list", and set it equal to the value of "string_lengths_cache" at the 'key' of "longest_length".
    
    (5) Return the value of "longest_strings_list".
"""

def allLongestStrings(inputArray):
    string_lengths_cache = {}
    longest_length = 0
    for i in inputArray:
        if len(i) in string_lengths_cache:
            string_lengths_cache[len(i)].append(i)
        else:
            string_lengths_cache[len(i)] = [i]
            if len(i) > longest_length:
                longest_length = len(i)
    longest_strings_list = string_lengths_cache[longest_length]
    
    return longest_strings_list
        