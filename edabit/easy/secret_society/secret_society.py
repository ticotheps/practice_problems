"""
SECRET SOCIETY

A group of friends have decided to start a secret society. The name of the
secret society will be the fist letter of each of their names, sorted in
alphabetical order.

UNDERSTAND PHASE:

Objective:
    - Create a function that takes in a list of friends' names, takes the first
    letter of each name, sorts them in alphabetical order, and returns the
    sorted first letters as the name of their secret society.

Expected Inputs & Outputs:
    - Inputs: 
        - Number: 1
        - Data Type: list
        - Name: "friends_list"
        
    - Outputs: 
        - Number: 1
        - Data Type: string
        - Name: "society_name"
        
Examples:
    (1) get_society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
    (2) get_society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
    (3) get_society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"
        
"""
"""
PLAN PHASE:
    (1) Create a function that takes in one input, 'friends_list', and returns
    one output, 'society_name'.
    
    (2) Create a variable, 'society_name', that will be returned as your output (data type: string).
    
    (3) Create a variable, 'friends_first_chars_list', that will contain all of the first characters of each name from the 'friends_list' input.
    
    (4) Use a 'for' loop to iterate through each name of the 'friends_list' input and extract the first letter of each name and then append that letter to the 'friends_first_chars_list'.
    
    (5) Use the '.sort()' method to sort all of the items in the 'friends_first_chars_list' in alphabetical order and set that value equal to a new variable, 'sorted_first_chars_list'.
    
    (6) Use the '.join()' method to join each of the items in the 'sorted_first_chars_list' and set that new string equal to 'society_name'.
    
    (7) Return 'society_name'
"""

def get_society_name(friends_list):
    # Creates a variable, 'friends_first_char_list', that will contain all of 
    # the first characters of each name from the 'friends_list' input.
    friends_first_chars_list = []
    
    # Iterates through each name of the 'friends_list' input and extracts
    # the first letter of each name and appends that letter to the 
    # 'friends_first_char_list'.
    for name in friends_list:
        # Gets access to first character of name
        first_char = name[0]
        
        # Adds that 'first_char' to the 'friends_first_chars_list'
        friends_first_chars_list.append(first_char)
        
    # Uses the '.sort()' method to sort all of the items in the 
    # 'friends_first_chars_list' in alphabetical order and sets it equal to a
    # new variable, 'sorted_first_chars_list'
    friends_first_chars_list.sort()
    sorted_first_chars_list = friends_first_chars_list
    
    # Uses the '.join()' method to join each of the items in the
    # 'sorted_first_chars_list' and sets that new string equal to
    # 'society_name'.
    society_name = ''.join(sorted_first_chars_list)
        
    return society_name
    

print(get_society_name(["Adam", "Sarah", "Malcolm"]))
print(get_society_name(["Harry", "Newt", "Luna", "Cho"]))
print(get_society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))