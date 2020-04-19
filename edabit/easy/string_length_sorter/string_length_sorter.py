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
    
    (2) Create a variable, 'string_len_dict', which will store a key:value 
        pair of string:string's length. Initialize this variable with an 
        empty dictionary.
    
    (3) Create a variable, 'string_len_list', that will store a new list of 
        string lengths that have been sorted from shortest to longest. Initialize this 
        variable with an empty Python list.
    
    (4) Use a 'for' loop to iterate through the 'strings_list' input list.
    
        (4a) Create a variable, 'string_len', that will store the integer value of
             the currently iterated on item from the list.
            
        (4b) Use the '.append()' method to add 'string_len' to the 'string_len_list'.

        (4c) Create a new dictionary entry for 'string_len_dict', where each string's 
             length is the key and each string's sequence of characters is the value in
             the 'key:value' pair.
            
    
    (5) Create a variable, 'sorted_string_len_list', that will store a sorted version
        of the 'string_len_list' using the 'sorted()' built-in Python method.
        
    (6) Create a variable, 'sorted_strings_list', that will store a new sorted list 
        of actual strings from the input list.
        
    (7) Use a 'for' loop that to iterate through each item in the 'sorted_string_len_list'.
        
        (7a) Create a new variable, 'sorted_string_value', and set it equal to the 
             retrieved string value of each iterated on 'string' item from the
             'sorted_string_len_list'.
             
        (7b) Use the '.append()' method to add the 'sorted_string_value' to the 
             'sorted_strings_list'.
             
    (8) Return the value of 'sorted_string_list'.
        
    
"""
# EXECUTE PHASE:

def sort_by_length(strings_list):
    print(f"\nOriginal List: {strings_list}")
    string_len_dict = dict()
    # print(string_len_dict)
    
    string_len_list = []
    # print(string_len_list)
    
    for string in strings_list:
        string_len = len(string)
        # print(string_len)
        
        string_len_list.append(string_len)
        
        string_len_dict[string_len] = string
        # print(string_len_dict[string_len])
        
    sorted_string_len_list = sorted(string_len_list)
    # print(sorted_string_len_list)
    
    sorted_strings_list = []
    
    for item in sorted_string_len_list:
        sorted_string_value = string_len_dict[item]
        # print(sorted_string_value)
        
        sorted_strings_list.append(sorted_string_value)
        
    print(f"New Sorted List: {sorted_strings_list}")
    return sorted_strings_list

sort_by_length(["Google", "Apple", "Microsoft"])
sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
sort_by_length(["Turing", "Einstein", "Jung"])

"""
REFLECT/REFACTOR PHASE:

Asymptotic Analysis:
    - Time Complexity: 
        - O(n log n)
        - Due to the built-in Python method, 'sorted()', having the most significant
          run time of each line in the algorithm.
          
    - Space Complexity: 
        - O(n)
        - Due to the Python dictionary that was created for fast lookup & retrieval.
"""