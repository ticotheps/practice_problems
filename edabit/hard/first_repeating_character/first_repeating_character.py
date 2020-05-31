"""
FIND FIRST CHARACTER THAT REPEATS

Create a function that takes a string and returns the first character that
repeats. If there is no repeat of a character, then return "-1".

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
    - Data Type: string or integer
    - Var Name: 'repeating_char'
    
Constraints:
    - Tests are case-sensitive.
        - i.e. - "I" != "i"

PHASE II: PLAN

Brute Force Solution (nested 'for' loops):
    (1) Define a function that takes in a single input string argument and
    returns a single output string or integer depending on the existence of
    repeating characters.
    
    (2) Declare a var, 'repeating_char', that will hold the first character that is found to repeat itself in the input string. Initialize this var with a value of '' (an empty string).
    
    (3) Use an outer 'for' loop to iterate through each character in the input string. This will provide access to each letter of the input string for comparison purposes.
    
    (4) Nest an inner 'for' loop inside of the outer 'for' loop to iterate through each of the same characters in the input string for a second time. This second iteration will enable each character to be compared to itself and to each of the other characters.
    
    (5) Inside of the inner 'for' loop, evaluate whether or not the iterated element, 'j'(of the inner 'for' loop), is a repeating character of the iterated element, 'i' (of the outer 'for' loop).
    
        (a) If it is a repeating character, set the value of 'repeating_char' equal to 'i'.
        
        (b) If it is NOT a repeating character, do nothing.
        
    (6) Return the value of 'repeating_char'.
    

PHASE III: EXECUTE (Please see below)

PHASE IV: REFLECT/REFACTOR
"""

def first_repeat(chars):
    print(f"\nchars = {chars}")
    
    repeating_char = None
    print(f"INITIAL repeating_char = {repeating_char}")
    
    for i in range(0, len(chars)):
        print(f"\ni = {chars[i]}")
        
        for j in range(0, len(chars)):
            if i != j:
                print(f"--- j = {chars[j]} ---")
                if chars[i] == chars[j]:
                    print(f"'{chars[j]}' is a repeating character of '{chars[i]}'")
                    repeating_char = chars[j]
                    print(f"UPDATED repeating_char = {repeating_char}")
                    return repeating_char

    print(f"No repeating characters were identified in the input string")
    repeating_char = -1
    return repeating_char
    
    
print(first_repeat('legolas'))  # -> 'l'
print(first_repeat('Gandalf'))  # -> 'a'
print(first_repeat('Balrog'))  # -> -1
print(first_repeat('Isildur'))  # -> -1