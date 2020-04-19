"""
Sort a List by String Length

Create a function that takes a list of strings and returns a list, sorted from
shortest to longest.
"""
"""
UNDERSTAND PHASE:

Objective: 
    - Create an algorithm, 'sort_by_length()' that takes in a single input (a Python list;
    'strings_list') and returns a single output (a Python list;
    'sorted_strings_list').
    
Expected Inputs & Outputs:
    - Inputs:
        - Expected Number: 1
            - Type: Python List
            - Name: 'strings_list'
    - Outputs:
        - Expected Number: 1
            - Type: Python List
            - Name: 'sorted_strings_list'
            
Constraints:
    - Can the input list be empty?
        - No.
    - Can there be multiple strings in the input list with the same length?
        - Assume that all inputs lists will contain strings of different lengths.
        
Examples:
    (1) sort_by_length(["Google", "Apple", "Microsoft"])  ->  ["Apple",
    "Google", "Microsoft"]
    (2) sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])  ->
    ["Raphael", "Leonardo", "Donatello",  "Michelangelo"]
    (3) sort_by_length(["Turing", "Einstein", "Jung"])  ->  ["Jung",
    "Turing", "Einstein"]
"""
"""
PLAN PHASE:
    (1) Create a function, 'sort_by_length()', that takes in 1 parameter,
    'strings_list', and returns a single value, 'sorted_strings_list'.
    (2) Create a variable, 'shortest_len', that will store the integer value
    of the shortest string's length. Initialize this variable with a value of 0.
    (3) Use a 'for' loop to iterate through the 'strings_list' input list.
        (4) Create a variable, 'string_len', that will store the integer value of
            the currently iterated on item from the list.
        (5) Evaluate whether or not the 'string_len' is greater than or less than
            the current value of 'shortest_len'.
            (6a)
"""
# EXECUTE PHASE:

"""
REFLECT/REFACTOR PHASE:
"""