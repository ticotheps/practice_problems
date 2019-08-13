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

import math

def checkPalindrome(inputString):
    str_length = len(inputString)
    num_ideal_matches = math.floor(str_length/2)
    num_real_matches = 0
    if (str_length > 0) and (str_length < 1000000):
        for i in range(math.floor(str_length/2)):
            front_counter = inputString[i]
            back_counter = inputString[str_length-i-1]
            # print(front_counter, back_counter)
            if front_counter == back_counter:
                num_real_matches += 1
                # print("We have a match")
        if num_real_matches == num_ideal_matches:
            # print("Total matches:", num_real_matches)
            return True
        else:
            return False
        
print(checkPalindrome("ooroo"))