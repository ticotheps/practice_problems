"""
PALINDROME CHECK

Write a function that takes in a non-empty string and that returns a boolean
representing whether the string is a palindrome. A palindrome is defined as "a
string that's written the same forward and backward. 

Note: Single character strings ARE palindromes.

Sample Input: "abcdcba"
Sample Output: "True"

Hints:
    - Start by building the input string in reverse order and comparing this
    newly built string to the input string.
    - Can you optimize your algorithm by using recursion? What are the
    implications of recursion on an algorithm's space-time complexity analysis?
    - Go back to an iterative solution and try using pointers to solve this
    problem: start with a pointer at the first index of the string and a pointer
    at the final index of the string. What can you do from there?
"""
"""
****** UNDERSTAND Phase ******
- Objective: 
    - Write an algorithm, "isPalindrome()", that takes in 1 input (string data
      type; "string"), evaluates the input, and then returns 1 output (Boolean 
      data type; True or False).
      
- Expected Input(s): 
    - Number Of: 1
    - Data Type: string
    - Var Name(s): "string"
    
- Expected Output(s): 
    - Number Of: 1
    - Data Type: Boolean
    - Var Name(s): "verified_palindrome"
    
- Edge Cases & Constraints:
    - Can the input string ever be empty?
        - No.
    - Can the string include non-alphabetic characters?
        - Yes.
    - How do you handle single character strings?
        - Treat them as palindromes.

****** PLAN + EXECUTE Phases ******
"""

def isPalindrome(string):
    verified_palindrome = True
    rev_string = string[::-1]
    for i in range(0, len(rev_string) - 1):
        if string[i] != rev_string[i]:    
            verified_palindrome = False
            return verified_palindrome
    return verified_palindrome