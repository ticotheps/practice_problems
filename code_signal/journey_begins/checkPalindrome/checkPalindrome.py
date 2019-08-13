# UNDERSTANDING THE PROBLEM
# Palindrome = word that is spelled the same backwards as it is forwards.

# Expected Input = a string (at least length of 1)
# Expected Output = True or False

# DEVISING A PLAN

# (1) Check the length of 'inputString'.
# (2) Use nested FOR loops to iterate from front => back in one FOR loop
#     and use the inner FOR loop to iterate from back => front to check
#     for matches at indices that are the same distance from each end
#     of the string.
# (3) If there is a match, continue to iterate towards the center from
#     both ends until either...
#     (4) ...there are no more matches...or
#     (5) ...the indices cross paths.


def checkPalindrome(inputString):
    str_length = len(inputString)
    
    if (str_length > 0) and (str_length < 1000000):
        print(str_length)
        
checkPalindrome("tico")