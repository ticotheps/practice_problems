"""
FILTER OUT STRINGS FROM AN ARRAY

Objective: 
    - Create a function that takes in a list of non-negative integers and
        strings and returns a new list without the strings.
        
Examples:
    - filter_out_strings([1, 2, "a", "b"]) -> [1, 2]
    - filter_out_strings([1, "a", "b", 0, 15]) -> [1, 0, 15]
    - filter_out_strings([1, 2, "aasf", "1", "123", 123]) -> [1, 2, 123]
    
Notes:
    - Zero is a non-negative integer.
"""

"""
UNDERSTAND PHASE


"""

# PLAN + EXECUTE PHASES

def filter_out_strings(input_list):
    return input_list

print(filter_out_strings([1, 2, "a", "b"])) # should print [1, 2]
print(filter_out_strings([1, "a", "b", 0, 15])) # should print [1, 0, 15]
print(filter_out_strings([1, 2, "aasf", "1", "123", 123])) # should print [1, 2, 123]

"""
REFLECT/REFACTOR PHASE

"""