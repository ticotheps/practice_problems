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

UNDERSTAND:
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
            
PLAN:

    (1) Create a function that takes in a single given input, 'hrs_int', and returns a single output, 'secs_int'.
    
    (2) Declare a variable, 'secs_int', that will store the 'hrs_int' equivalent number of seconds.
    
    (3) Convert the number of hours from 'hrs_int' into an equivalent number of seconds that will be
    stored in the 'secs_int' variable from step 2.
    
    (4) Return the value of 'secs_int' and make sure the data type is of 'integer' type.

"""

# EXECUTE:

def how_many_seconds(hrs_int):
    pass

# REFLECT/REFACTOR: