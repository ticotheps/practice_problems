"""
YOU FAILEDPASSED THE EXAM

Here is what you see after you take your exam:
`Your Score: 85%

You FAILEDPASSED the Exam.

Required Score 85%`

The challenge is to fix all of the bugs in this incredible messy code, which the
code in the image might've actually looked like (probably not)! The code given
will output the same middle two lines as in the image shown above.
    - First parameter is the user's score.
    - Second parameter is the required score.
    
Examples:
    - grade_percentage("85%", "85%") ➞ "You PASSED the Exam"
    - grade_percentage("99%", "85%") ➞ "You PASSED the Exam"
    - grade_percentage("65%", "90%") ➞ "You FAILED the Exam"
    
Notes:
    - Note that inputs will be given as a string percentage number.
    - Maintain all capitalization.
    - Feel free to declutter and refactor code if it helps!
"""

"""
***** UNDERSTAND PHASE *****
- Objective: 
    - Fix the starter code that was provided so that it outputs the proper
      statement when a user passes an exam and when a user fails an exam.
      
- Expected Inputs:
    - Number Of: 2
    - Data Type: string, string
    - Var Names: "user_score", "pass_score"
    
- Expected Outputs:
    - Number Of: 1
    - Data Type: string
    - Var Names: None
    
- Edge Cases & Constraints:
    - None

***** PLAN PHASE *****
- Brute Force Solution:
    (1) Define a function that takes in two inputs ("user_score", "pass_score")
    and returns a single output (an 'f-string') that determines whether or not a
    user "PASSED" or "FAILED" their exam.
    
    (2) Declare a var, "result", and initialize it with an empty string.
    
    (3) If the "user_score" was LESS THAN the "pass_score", set the value of
    "result" to "FAILED".
    
    (4) If the "user_score" was GREATER THAN the "pass_score", set the value of
    "result" to "PASSED".
    
    (5) Return an f-string that says: "You {result} the Exam".

***** EXECUTE PHASE ***** (Please see below)
"""

# Python3 compatibile solution
def grade_percentage(user_score, pass_score):
    result = ""
    
    if int(user_score[:-1]) < int(pass_score[:-1]):
        result = "FAILED"
    
    if int(user_score[:-1]) >= int(pass_score[:-1]):
        result = "PASSED"
    
    return f"You {result} the Exam"

# Python2 compatible solution
# def grade_percentage(user_score, pass_score):
#     passed = "PASSED"
# 	failed = "FAILED"
	
# 	if int(user_score[:-1]) < int(pass_score[:-1]):
# 		return "You %s the Exam" % (failed)
	
# 	if int(user_score[:-1]) >= int(pass_score[:-1]):
# 		return "You %s the Exam" % (passed)
    
print(grade_percentage("85%", "85%"))  # "You PASSED the Exam"

"""
***** REFLECT/REFACTOR PHASE *****
- Asypmtotic Analysis:
    - Brute Force Solution:
        - Time Complexity: O(1) -> "constant time"
        - Space Complexity: O(1) -> "constant space"
        
    - Can/should we improve the time/space complexity of the Brute Force
      Solution?
        - Nope. O(1) is pretty darn good for both time & space complexity!
"""

