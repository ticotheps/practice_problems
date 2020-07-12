"""
LETTERS ONLY

Write a function that removes any non-letters from a string, returning a
well-known film title.

Examples:
    - letters_only("R!=:~0o0./c&}9k`60=y") ➞ "Rocky"
    - letters_only("^,]%4B|@56a![0{2m>b1&4i4") ➞ "Bambi"
    - letters_only("^U)6$22>8p).") ➞ "Up"

"""
"""
The 4 Phases of the U.P.E.R. Problem-Solving Framework:

U = UNDERSTAND Phase
P = PLAN Phase
E = EXECUTE Phase
R = REFLECT/REFACTOR Phase

***** The UNDERSTAND Phase *****
- Objective:
    - Write an algorithm that takes in a single input string, removes any
      non-alphabetic characters, and returns a single output string (which also
      happens to be a well-known film title).
      
- Expected Input(s):
    - Number Of: 1
    - Data Type: string
    - Var Name: "txt"
    
- Expected Output(s):
    - Number Of: 1
    - Data Type: string
    - Var Name: "movie_title"
    
- Edge Cases & Constraints:
    - Can the given input string be empty?
        - Yes. If so, we will return a string that says, "Invalid input. Please
          provide a non-empty input string."
    - Can the input be any other data type besides a string?
        - No. If so, we will return a string that says, "Invalid input. Please
          provide an input of string data type."

***** The PLAN & EXECUTE Phases (please see below) *****
"""
# FIRST PASS SOLUTION

# (1) Define a function that takes in 1 input, 'txt', and returns 1 output, 
# 'movie_title'.
def letters_only(txt):
    # (2) Declare a var, 'movie_title_list', and initialize it with a pair of 
    # empty square brackets.
    movie_title_list = []
    print(f"**INITIAL** movie_title_list = {movie_title_list}")
    
    # (3) Evaluate the given input string, ensuring that it isn't empty.
    if txt == "":
        return "Invalid input. Please provide a non-empty input string."
    
    # (4) Evaluate the given input string, ensuring that it is of string data 
    # type.
    if type(txt) != str:
        return "Invalid input. Please provide an input of string data type."
    
    # (5) Use a 'for' loop to iterate through each char of the given input
    # string.
    for char in txt:
        # (5a) If the char is alphabetic, append it to the 'movie_title' list.
        if char.isalpha() == True:
            movie_title_list.append(char)
            print(f"**UPDATED** movie_title_list = {movie_title_list}")
        # (5b) Else, print a string saying that the char is not alphabetic.
        else:
            print(f"{char} is not an alphabetic character.")
    # (6) Convert the 'movie_title_list' from a list to a string and return it.
    return "".join(movie_title_list)

print(letters_only(''))  # 'Invalid input. Please provide a non-empty input string.'
print(letters_only(23))  # 'Invalid input. Please provide an input of string data type.'
print(letters_only('R!=:~0o0./c&}9k`60=y'))  # 'Rocky'

"""
***** The REFLECT/REFACTOR Phase *****
- Asymptotic Analysis:
    - FIRST PASS SOLUTION:
        - Time Complexity: O(n^2) -> "quadratic"
        - Space Complexity: O(1) -> "constant"
"""

