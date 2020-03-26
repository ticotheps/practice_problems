"""
Is it Time for Milk and Cookies?

Christmas Eve is almost upon us, so naturally we need to prepare some milk and
cookies for Santa! Create a function that accepts a Date object and returns True
if it's Christmas Eve (December 24th) and False otherwise.

Objective: 
    - Write an algorithm that takes in a single input, 'date', and can
    return a single output (either "True" or "False").

Expected Inputs & Outputs:
    - Inputs:
        - Number: 1
        - Data Type: Python Dictionary (object)
        - Name: 'date_dict'
        
    - Outputs:
        - Number: 1
        - Data Type: Python Bool (Boolean value)
        - Name: 'Christmas_eve'
        
    - Constraints:
        - Assume that all test cases will contain valid dates.
        
    - Examples:
        - time_for_milk_and_cookies(datetime.date(2013, 12, 24)) ➞ True
        - time_for_milk_and_cookies(datetime.date(2013, 1, 23)) ➞ False
        - time_for_milk_and_cookies(datetime.date(3000, 12, 24)) ➞ True
        
Plan:
    (1) Create a function that takes in a single input (Python dictionary),
    'date_dict', and returns a single output (Python bool), 'Christmas_eve'. 
    
    (2) Create a variable, 'Christmas_eve', that is initialized with a value of False. This variable will be returned as the output.
    
    (3) Convert the 'date_dict' input from an object to a viewable Python string using the 'str()' method and set it equal to a new variable, 'date_str'.
    
    (4) Convert the 'date_str' string into a list of items separated by '-' using the '.split()' method and set it equal to a new variable, 'date_items_list'.
    
    (5) Use a conditional 'if' statement to determine if the passed in 'date_items_list' contains the string, '24', in it.
    
        (6a) If it does, return True.
        
        (6b) If it doesn't, return False.
"""

import datetime

# takes in a date dictionary and returns True or False, depending on if the date
# falls on Christmas Eve Day.
def time_for_milk_and_cookies(date_dict):
    # returned output
    Christmas_eve = False
    
    # converts input dictionary into a Python string
    date_str = str(date_dict)
    # print(f"date_str = {date_str}")
    
    # splits converted string into a list of items (separated by hyphens)
    date_items_list = date_str.split('-')
    # print(f"date_items_list = {date_items_list}")
    
    # checks to see if 
    if '24' in date_items_list:
        return True
    else:
        return False
    
    return date_dict

# my_date1 = datetime.date(2020, 3, 26) # False
# my_date2 = datetime.date(2020, 3, 24) # True
# my_date3 = datetime.date(2020, 3, 25) # False

# print(time_for_milk_and_cookies(my_date1))
# print(time_for_milk_and_cookies(my_date2))
# print(time_for_milk_and_cookies(my_date3))