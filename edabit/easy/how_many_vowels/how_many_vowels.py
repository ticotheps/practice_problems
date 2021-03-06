"""
How Many Vowels?

Create a function that takes a string and returns the number (count) of vowels
contained within it.

Examples:
print(count_vowels("Celebration")) ➞ 5

print(count_vowels("Palm")) ➞ 1

print(count_vowels("Prediction")) ➞ 4

NOTES:
- The following characters are considered "vowels": a, e, i, o, u (not y).
- All test cases are ONE word and only contain letters.
"""

# Objective: Find total sum of all "vowels" in the given input string.

# Constraints: 
# - Only the following are "vowels" => a, e, i, o, u (not y).
# - All given inputs will be void of spaces and will only contain letters.

# Plan: 
#   (1) Create a function that takes in 1 input ('txt' => a String) and returns
#       1 output ('num_of_vowels' => an Integer). 

#   (2) Create a dictionary, 'vowels_dict', that contains 'key:value' pairs 
#       where the 'key' is an accepted "vowel" character and the 'value' 
#       is the 'True' Bool value.

#   (3) Create a 'num_of_vowels' variable that will store the running total
#       number of vowels. 

#   (4) Use a 'for' loop to iterate through the given input 'txt'.

#   (5) Create a 'lower_char' variable that converts the character at the 
#       current index to a lower-cased version of itself.

#   (6) Use a conditional statement to determine if the value of 'lower_char' 
#       at the current index, i, exists in the 'vowels_dict' dictionary. If it
#       exists, add 1 to the 'num_of_vowels' dictionary. If it does not exist, 
#       skip to the next iteration.

#   (7) Return the value for the 'num_of_vowels' variable.

# Implementation:
def count_vowels(txt):
    vowels_dict = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }
    num_of_vowels = 0
    
    for i in range(0, len(txt)):
        char = txt[i]
        lower_char = char.lower()
        
        if lower_char in vowels_dict:
            num_of_vowels += 1
            
    return(num_of_vowels)

print(count_vowels('Celebration'))  # Should return 5
print(count_vowels('Palm'))  # Should return 1
print(count_vowels('Prediction'))  # Should return 4