"""
FIND FIRST CHARACTER THAT REPEATS

Create a function that takes a string and returns the first character that
repeats. If there is no repeat of a character, then return '-1' (string).

Examples:
    - first_repeat('legolas') -> 'l'
    - first_repeat('Gandalf') -> 'a'
    - first_repeat('Balrog') -> '-1'
    - first_repeat('Isildur') -> '-1'  // Case-sensitive 'I' != 'i'
    
Notes:
    - Tests are case-sensitive.
"""
"""
U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND

Objective:
    - Write an algorithm that takes in a single input (of string data type) and
    returns a single output (of string or integer data type).
    
Expected Input(s):
    - Number Of: 1
    - Data Type: string
    - Var Name: 'input_str'
    
Expected Output(s):
    - Number Of: 1
    - Data Type: string
    - Var Name: 'repeating_char'
    
Constraints:
    - Tests are case-sensitive.
        - i.e. - "I" != "i"

PHASE II: PLAN

Brute Force Solution (nested 'for' loops):
    (1) Define a function that takes in a single input string argument and
    returns a single output string or integer depending on the existence of
    repeating characters.
    
    (2) Declare a var, 'repeating_char', that will hold the first character that is found to repeat itself in the input string. Initialize this var with a value of None.
    
    (3) Use an outer 'for' loop to iterate through each character in the input string. This will provide access to each letter of the input string for comparison purposes.
    
    (4) Nest an inner 'for' loop inside of the outer 'for' loop to iterate through each of the same characters in the input string for a second time. This second iteration will enable each character to be compared to itself and to each of the other characters.
    
    (5) Inside of the inner 'for' loop, evaluate whether or not the iterated element, 'j'(of the inner 'for' loop), is a repeating character of the iterated element, 'i' (of the outer 'for' loop).
    
        (a) If it is a repeating character, set the value of 'repeating_char' equal to 'i'.
        
        (b) If it is NOT a repeating character, do nothing.
        
    (6) If no repeating characters were found, set the value of 'repeating_char' to '-1'.
        
    (7) Return the value of 'repeating_char'.
    

PHASE III: EXECUTE (Please see below)

PHASE IV: REFLECT/REFACTOR

Brute Force Solution:
    - Asymptotic Analysis:
        - Time Complexity: O(n^2) -> 'quadratic'
        - Space Complexity: O(1) -> 'constant'
        
    - Could we improve the time or space complexity of this solution?
        - Yes. We could cache characters in a python dictionary by ensuring that a key:value pair exists in the dictionary for each character. The lookup for dictionaries is O(1) time complexity.
        - Please see the first_repeate_optimized() solution below.
"""

def first_repeat(chars):
    repeating_char = None
    
    for i in range(0, len(chars)):
        
        for j in range(0, len(chars)):
            if i != j:
                if chars[i] == chars[j]:
                    repeating_char = chars[j]
                    print(f"repeating_char = {repeating_char}")
                    return repeating_char
    repeating_char = '-1'
    print(f"repeating_char = {repeating_char}")
    return repeating_char

def first_repeat_optimized(chars):
    cache = {}
    repeating_char = None
    
    for i in range(0, len(chars)):
        if chars[i] not in cache:
            cache[chars[i]] = True
        else:
            repeating_char = chars[i]
            print(f"repeating_char = {repeating_char}")
            return repeating_char
    repeating_char = '-1'
    print(f"repeating_char = {repeating_char}")
    return repeating_char