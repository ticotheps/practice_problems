"""
CONVERT HOURS INTO SECONDS

Write a function that converts hours into seconds.

Examples:
    - how_many_seconds(2) -> 7200
    - how_many_seconds(10) -> 36000
    - how_many_seconds(24) -> 86400
    
Notes:
    - 60 seconds in a minute; 60 minutes in a hour.
    - Don't forget to return your answer.
"""

"""
U.P.E.R.

(A) UNDERSTAND:
    - Objective:
        - Write an algorithm that takes in a single input integer (representing a
        given number of hours) and returns a single output (representing the 
        equivalent number of seconds).
    
    - Expected Inputs:
        - Number: 1
        - Data Type: integer
        - Variable Name: 'hrs_int'
        
    - Expected Outputs:
        - Number: 1
        - Data Type: integer
        - Variable Name: 'secs_int'
        
    - My Examples:
        - how_many_seconds(1) -> 3600
            - 1 hr * (60 min/1 hr) * (60 sec/1 min) = 3600 secs
        - how_many_seconds(5) -> 18000
            - 5 hr * (60 min/1 hr) * (60 sec/1 min) = 18000 secs
        - how_many_seconds(12) -> 43200
            - 12 hr * (60 min/1 hr) * (60 sec/1 min) = 43200 secs

    - Edge Cases & Constraints to Consider:
        - Can the input be negative?
            - No, because time is measured in positive units. The input must be greater than 0.
        - Can the input be a floating point number?
            - Yes, because the number of hours doesn't need to be whole in order
            to find an equivalent number of seconds.
        - Can the input be None?
            - No, because you cannot convert 'None' number of hours.
            
(B) PLAN:

    (1) Create a function that takes in a single given input, 'hrs_int', and returns a single output, 'secs_int'.
    
    (2) Assign the value of 'None' to two new variables, 'mins_int' and 'secs_int'.
    
    (3) Make sure that a conversion of hours to seconds will NOT occur unless the given input, 'hrs_int', is in fact of either "integer" or "float" data type.

        (a) If the given input, 'hrs_int', is a valid argument, proceed with converting the given number of hours into an equivalent number of seconds.
        
            i. Convert the number of hours in 'hrs_int' into an equivalent number of minutes and store that value in the previously declared 'mins_int' variable.
            
            ii. Convert the number of minutes in 'mins_int' into an equivalent number of seconds and store that value in the previously declared 'secs_int' variable.
        
        (b) If the given input, 'hrs_int', is an INVALID argument (i.e. - negative value, not of 'integer' or 'float' data types, null), handle the error with a 'TypeError' exception.
    
    (4) Return the value of 'secs_int'.

"""

# (C) EXECUTE:

def how_many_seconds(hrs_int):
    mins_int = None
    secs_int = None
    
    if hrs_int > 0 and hrs_int is not None:
        mins_int = hrs_int * 60     # converts given hours into minutes
        secs_int = mins_int * 60    # converts given minutes into seconds
    else: 
        raise TypeError("Invalid input type")

    return secs_int

# (D) REFLECT/REFACTOR: