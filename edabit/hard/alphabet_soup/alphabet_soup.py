"""
ALPHABET SOUP

Create a function that takes in a string and returns a string with its letters
in alphabetical order.

Examples:
    - alphabet_soup("hello") ➞ "ehllo"
    - alphabet_soup("edabit") ➞ "abdeit"
    - alphabet_soup("hacker") ➞ "acehkr"
    - alphabet_soup("geek") ➞ "eegk"
    - alphabet_soup("javascript") ➞ "aacijprstv"
    
Notes:
    - You can assume numbers and punctuation symbols won't be included in test
    cases. You'll only have to deal with single word, alphabetic characters.
"""

"""
The U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND

- Objective(s): 
    - Write an algorithm that takes in a string (of alphabetic characters only)
      and returns a new string with all of the letters from the given input in 
      alphabetized order.
      
- Expected Input:
    - Number Of: 1
    - Data Type: string
    - Var Name: 'str'
    
- Expected Output:
    - Number Of: 1
    - Data Type: string
    - Var Name: 'new_str'
    
- Edge Cases & Constraints:
    - Can the given input be an empty string?
        - No.
    - Can the given input string include non-alphabetic characters?
        - No. Assume that the characters in the given input will only be
          alphabetic characters.

PHASE II: PLAN

- First-Pass Solution:
    (1) Define a function that takes in a single input string of alphabetic 
    characters, 'str', and returns a single output, 'new_str', which is a 
    modified version of the original given input string where all the characters
    are alphabetized.
    
    (2) Declare a var, 'alphabet', and initialize it with a list that includes
    each letter of the alphabet (Upper-case & lower-case).
    - i.e. - [
        A, a, 
        B, b, 
        C, c, 
        D, d, 
        E, e, 
        F, f, 
        G, g, 
        H, h, 
        I, i, 
        J, j, 
        K, k,
        L, l, 
        M, m, 
        N, n, 
        O, o, 
        P, p, 
        Q, q, 
        R, r, 
        S, s, 
        T, t, 
        U, u, 
        V, v,
        W, w,
        X, x,
        Y, y,
        Z, z 
      ]
      
    (3) Declare a var, 'new_str', and initialize it with an empty string ('').
    
    (4) Use a 'for' loop to iterate through each letter of the 'alphabet' list.
    
        (a) Use another nested 'for' loop to iterate through each character from
        the given input string, 'str'.
        
            (i) If the iterated-on character from 'str' matches the iterated-on
            letter from 'alphabet', concatenate the former on to the 'new_str' 
            string.
            
            (ii) Otherwise, do nothing.
            
    (5) Return the value of 'new_str'.
    
    
PHASE III: EXECUTE (Please see below)

PHASE IV: REFLECT/REFACTOR

- First-Pass Solution:
    - Asymptotic Analysis:
        - Time Complexity: O(n^2) -> 'quadratic'
        - Space Complexity: O(1) -> 'constant'

    - Can you improve the time or space complexity of this solution?
        - Yes.
        - How?
            - Use a cache object instead of a list for faster lookups.
"""

def alphabet_soup(str):
    alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f',
                'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l',
                'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r',
                'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x',
                'Y', 'y', 'Z', 'z']
    
    new_str = ''
    
    for i in alphabet:
        # print(f"i = {i}")
        
        for j in str:
            # print(f"j = {j}")
            
            if j == i:
                # print(f"j ({j}) == i ({i})")
                new_str += f"{j}"
    
    return new_str

print(alphabet_soup('hello'))  # 'ehllo'
print(alphabet_soup('edabit'))  # 'abdeit'
print(alphabet_soup('hacker'))  # 'acehkr'
print(alphabet_soup('geek'))  # 'eegk'
print(alphabet_soup('javascript'))  # 'aacijprstv'

def alphabet_soup_optimized(str):
    alphabet = {
        'A': True, 
        'a': True,
        'B': True,
        'b': True,
        'C': True, 
        'c': True, 
        'D': True, 
        'd': True, 
        'E': True, 
        'e': True, 
        'F': True, 
        'f': True,
        'G': True, 
        'g': True, 
        'H': True, 
        'h': True, 
        'I': True, 
        'i': True, 
        'J': True, 
        'j': True, 
        'K': True, 
        'k': True, 
        'L': True, 
        'l': True,
        'M': True, 
        'm': True, 
        'N': True, 
        'n': True, 
        'O': True, 
        'o': True, 
        'P': True, 
        'p': True, 
        'Q': True, 
        'q': True, 
        'R': True, 
        'r': True,
        'S': True, 
        's': True, 
        'T': True, 
        't': True, 
        'U': True, 
        'u': True, 
        'V': True, 
        'v': True, 
        'W': True, 
        'w': True, 
        'X': True, 
        'x': True,
        'Y': True, 
        'y': True, 
        'Z': True, 
        'z': True
    }
    
    new_str = ''
    
    for key in alphabet:
        # print(f"key = {key}")
        
        for j in str:
            # print(f"j = {j}")
            
            if j == key:
                # print(f"j ({j}) == key ({key})")
                new_str += f"{j}"
    
    return new_str

print(alphabet_soup_optimized('hello'))  # 'ehllo'
print(alphabet_soup_optimized('edabit'))  # 'abdeit'
print(alphabet_soup_optimized('hacker'))  # 'acehkr'
print(alphabet_soup_optimized('geek'))  # 'eegk'
print(alphabet_soup_optimized('javascript'))  # 'aacijprstv'