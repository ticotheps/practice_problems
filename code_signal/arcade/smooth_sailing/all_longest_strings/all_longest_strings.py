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
    print(f"\nstring_lengths_cache = {string_lengths_cache}")
    
    longest_length = 0
    print(f"longest_length = {longest_length}")
    
    for i in inputArray:
        print(f"\ni = {i}")
        
        if len(i) in string_lengths_cache:
            string_lengths_cache[len(i)].append(i)
        else:
            string_lengths_cache[len(i)] = [i]
            if len(i) > longest_length:
                longest_length = len(i)
                print(f"***longest_length = {longest_length}")    

        print(f"***string_lengths_cache = {string_lengths_cache}")
        
    longest_strings_list = string_lengths_cache[longest_length]
    print(f"longest_strings_list = {longest_strings_list}")
    
    return longest_strings_list


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))  # ["aba", "vcd", "aba"]
        