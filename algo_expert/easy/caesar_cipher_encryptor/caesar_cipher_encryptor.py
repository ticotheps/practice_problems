"""
CAESAR CIPHER ENCRYPTOR

Given a non-empty string of lowercase letters and a non-negative integer
representing a key, write a function that returns a new string obtained by
shifting every letter in the input string by k positions in the alphabet, where
k is the key.

NOTE:
    - Letters should "wrap" around the alphabet; in other words, the letter "z"
    shifted by one returns the letter "a".
    
Sample Inputs: "xyz", 2
Sample Output: "zab"

Hints:
    - Most languages have built-in functions that give you the Unicode value of
    a character as well as the character corresponding to a Unicode value.
    
    - Consider using such functions to determine which letters the input
    string's letters should be mapped to.
    
    - Try creating your own mapping of letters to codes. In other words, try
    associating each letter in the alphabet with a specific number - its
    position in the alphabet, for instance - and using that to determine which
    letters the input string's letters should be mapped to.
    
    - How do you handle cases where a letter gets shifted to a position that
    requires wrapping around the alphabet? What about cases where the key is
    very large and causes multiple wrappings around the alphabet? The modulo
    operator should be your friend here.
    
    - O(n) time | O(n) space - where n is the length of the input string
"""
"""
****** UNDERSTAND Phase ******
- Objective: Write an algorithm that takes in two inputs, a string of lowercase
  letters and an integer represting the number of positions to shift each letter
  forwards in the alphabet, and returns a new string with the shifted characters.

****** PLAN Phase ******
- First Pass Solution:
    (1) Define a function that takes in 2 inputs (string, integer) and returns 1
    output (string).
    
    (2) Declare a var, "new_string_list", and intitialize it with an empty list.
    
    (3) Use a 'for' loop to iterate through the given input string where the
    iterator will be "char"...
    
        (a) Declare a var, "uni_of_char", and initialize it with the Unicode value for 
        "string[i]" using the ".ord()" built-in Python function.
        
        (b) Declare a var, "new_char_uni", and initialize it with the Unicode value of "uni_of_char" + "key" (given input).
        
        (c) Declare another var, "new_char", and initialize it with the matching character using the ".chr()" built-in Python method.
        
        (d) Append the "new_char" to the "new_string_list".
        
    (4) Join all of the elements in the "new_string_list" using the ".join()"
    built-in Python method and set it equal to a new var, "new_string".
    
    (5) Return the value of "new_string".

****** EXECUTE Phase ******

****** REFLECT/REFACTOR Phase ******
"""

def caesarCipherEncryptor(string, key):
    # for i in string:
    uni = ord(string[0])
    print(f"UNICODE for '{string[0]}' = {uni}")
    print(f"CHAR for unicode 120 = {chr(120)}")

print(caesarCipherEncryptor("xyz", 2))  # "zab"