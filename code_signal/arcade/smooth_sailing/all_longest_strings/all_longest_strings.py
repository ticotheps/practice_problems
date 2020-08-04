"""
ALL LONGEST STRINGS

Given an array of strings, return another array containing all of its longest
strings.

Example:
    - Example Input: ["aba", "aa", "ad", "vcd", "aba"]
    - Example Output: ["aba", "vcd", "aba"]
"""

"""
UNDERSTAND & PLAN Phases
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
        