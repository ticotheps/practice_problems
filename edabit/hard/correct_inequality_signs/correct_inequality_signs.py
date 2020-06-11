"""
CORRECT INEQUALITY SIGNS

Create a function that returns True if a given inequality expression is correct
and False otherwise.
"""

"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND the problem

- Objective:
    - Write an algorithm that takes in a single string (containing a series of
      inequality expressions) as the input and returns a Boolean value as the
      output.
        - If the inequality expression inside of the input string is correct,
          return True.
        - Otherwise, return False.

- Expected Input(s):
    - Number Of: 1
    - Data Type(s): string
    - Var Name(s): 'txt'

- Expected Output(s):
    - Number Of: 1
    - Data Type(s): Boolean
    - Var Name(s): 'is_correct'

- Constraints:
    - Can the given input string include negative numbers?
        - Yes.

    - Can the given input string include floating point numbers?
        - Yes.

    - Can the given input be an empty strings?
        - Yes.

    - If given an empty string, how would you handle that input?
        - Return a string that says, 'Invalid input. The given input string
          cannot be empty.'

    - Can the given input NOT be of a string data type?
        - No. It must be a string.

    - If given an input of a different data type than 'string' (i.e. - integer,
      floating point number, list, etc.), how would you handle it?
        - Return a string that says, "Invalid input. The given input must be of
          'string' data type."

PHASE II: devise a PLAN

- First Pass Solution: 

    (1) Define a function that takes in a single input, 'txt', and returns a
    single output, 'is_correct'.

    (2) Validate the given input to ensure that it is of 'string' data type.

        (a) If it is not of a 'string' data type, return a string that says,
        "Invalid input. The given input must be of 'string' data type."

        (b) Otherwise, do nothing.

    (3) Declare a var, 'is_correct', and initialize it with 'False' (Boolean
    value).

    (4) Declare another var, 'txt_split_list', and initialize it with the value
    of "txt.split(' ')".

    (5) Validate the length of 'txt_split_list' to ensure that there is an odd
    number of elements in it.

        (a) If there is an EVEN number of elements in it, return a string that says, 'Invalid input. Please provide an input of string with a valid number of integers and operators in it.'

        (b) If there is an ODD number of elements in it, do nothing.

    (6) Declare a var, 'txt_nums_list', and initialize it with an empty pair of
    square brackets.

    (7) Declare a var, 'txt_operators_list', and initialize it with an empty
    pair of square brackets.  

    (8) Iterate through odd-numbered indices of the 'txt_split_list' with a 'for' loop.

        (a) Declare a var, 'num', and set its value equal to the element 
        (from 'txt_split_list') being iterated on.

        (b) Append 'num' to the 'txt_nums_list'.
        
    (9) Iterate through even-numbered indices of the 'txt_split_list' with a 'for' loop.

        (a) Declare a var, 'operator', and set its value equal to the element 
        (from 'txt_split_list') being iterated on.

        (b) Append 'operator' to the 'txt_operators_list'.

    (10) Declare a var, 'valid_operators_cache', and initialize it with the
    following values: 
        {
            '<': True,
            '>': True,
            '==': True,
            '<=': True,
            '>=': True,
            '!=': True
        }

    (11) Declare a var, 'all_operators_valid', and initialize it with a value of
    True (Boolean).

    (12) Iterate through each element of the 'txt_operators_list' with a 'for'
    loop.

        (13) Use an 'if' statement and the 'valid_operators_cache' to validate each element.

            (a) If the element is NOT a valid operator, update the value of 
            'all_operators_valid' to be False (Boolean).
            
            (b) Else, do nothing.
            
    (14) Declare a var, 'index_num_1', and initialize it with a value of 0
    (integer).
    
    (15) Declare a var, 'index_num_2', and initialize it with a value of 'index_num_1
    + 1' (integer).
    
    (16) Declare a var, 'index_operator', and initialize it with a value of 0
    (integer).
    
    (17) Iterate through a range (start = index_num_1, stop = len(txt_nums_list)) using
    a 'while' loop and vars 'index_num_1', 'index_num_2', and 'index_operator'.
    
        (a) Declare a var, 'valid_comparison', and initialize it with True (Boolean).
    
        (b) Declare a var, 'num_1', and initialize it with a value of 
        'int(txt_nums_list[index_num_1])'.
        
        (c) Declare a var, 'num_2', and initialize it with a value of 
        'int(txt_nums_list[index_num_2])'.
        
        (d) Declare a var, 'comparison_operator', and initialize it with a value 
        of 'txt_operators_list[index_operator]'.
        
        (e) Declare a var, 'compare_nums', and set it equal to 'num_1 + 
        comparison_operator + num_2'.
        
        (f) If 'compare_nums' is False, update 'valid_comparison' to be False 
        (Boolean) and return the value of 'is_correct'.
        
        (g) Else, do nothing.
        
        (h) Add 1 to the value of 'k' (iterator).
        
    (18) Update the value of 'is_correct' to be True (Boolean).

    (19) Return the value of 'is_correct'.


PHASE III: EXECUTE the plan (Please See Below)

PHASE IV: REFLECT on/REFACTOR the plan
"""

def correct_signs(txt):
    # print(f"\ntxt = {txt}")
    # print(f"type(txt) = {type(txt)}")
    
    is_correct = False
    # print(f"is_correct = {is_correct}")
    
    if type(txt) != str:
        return 'Invalid input. Please provide an input of string data type.'
    
    txt_split_list = txt.split(' ')
    # print(f"txt_split_list = {txt_split_list}")
    
    if len(txt_split_list) % 2 == 0:
        return 'Invalid input. Please provide an input of string with a valid number of integers and operators in it.'
    
    txt_nums_list = []
    # print(f"txt_nums_list = {txt_nums_list}")
    
    txt_operators_list = []
    # print(f"txt_operators_list = {txt_operators_list}")
    
    for i in range(0, len(txt_split_list), 2):
        num = txt_split_list[i]
        # print(f"num = {num}")
        
        txt_nums_list.append(num)
        # print(f"*UPDATED* txt_nums_list = {txt_nums_list}")
        
    for j in range(1, len(txt_split_list), 2):
        operator = txt_split_list[j]
        # print(f"operator = {operator}")
        
        txt_operators_list.append(operator)
        # print(f"*UPDATED* txt_operators_list = {txt_operators_list}")
        
    valid_operators_cache = {
        '<': True,
        '>': True,
        '==': True,
        '<=': True,
        '>=': True,
        '!=': True,
    }
    # print(f"valid_operators_cache = {valid_operators_cache}")
    
    all_operators_valid = True
    # print(f"all_operators_valid = {all_operators_valid}")
    
    for operator in txt_operators_list:
        # print(f"operator = {operator}")
        # print(f"type(operator) = {type(operator)}")
        
        if operator not in valid_operators_cache:
            all_operators_valid = False
            # print(f"'{operator}' is not considered a valid operator.")
            return is_correct
            
    # print("All operators from the 'txt_operators_list' were considered valid!")
    
    k = 0
    while k < len(txt_nums_list) - 1:
        valid_comparison = True
        # print(f"valid_comparison = {valid_comparison}")
        
        index_num_1 = k
        index_num_2 = k + 1
        index_operator = k
        
        num_1 = int(txt_nums_list[index_num_1])
        # print(f"num_1 = {num_1}")
        
        comparison_operator = txt_operators_list[index_operator]
        # print(f"comparison_operator = {comparison_operator}")
        
        num_2 = int(txt_nums_list[index_num_2])
        # print(f"num_2 = {num_2}")
        
        if comparison_operator == '<':
            compare_nums = num_1 < num_2
            
        elif comparison_operator == '>':
            compare_nums = num_1 > num_2
            
        elif comparison_operator == '==':
            compare_nums = num_1 == num_2
            
        elif comparison_operator == '<=':
            compare_nums = num_1 <= num_2
            
        elif comparison_operator >= '>=':
            compare_nums = num_1 >= num_2
            
        elif comparison_operator == '!=':      
            compare_nums = num_1 != num_2
        # print(f"compare_nums = {compare_nums}")
        
        if compare_nums == False:
            valid_comparison = False
            # print(f"This comparison, {str(num_1)} {comparison_operator} {str(num_2)}, in invalid.")
            return is_correct
        
        k += 1
        
    is_correct = True
    return is_correct


print(correct_signs(3)) # 'Invalid input. Please provide an input of string data type.'
print(correct_signs("3 < 7 < 11"))          # True
print(correct_signs("3 < 7 <")) # 'Invalid input. Please provide an input of string with a valid number of integers and operators in it.'
print(correct_signs("13 > 44 > 33 > 1"))    # False
print(correct_signs("1 < 2 < 6 < 9 > 3"))   # True