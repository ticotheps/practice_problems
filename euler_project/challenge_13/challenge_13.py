# Understanding the Problem
  # - Objective:  Return the first ten digits of the LARGE sum that is produced
  #             when adding together the given one-hundred 50-digit numbers.
  
  # Expected Inputs: 
    # - Number of Expected Inputs: 1
    # - Data Type of Expected Input: array (of large numbers)
    
  # Expected Outputs:
    # - Number of Expected Outputs: 1
    # - Data Type of Expected Input: integer (1st 10 digits of very large sum)
    
a = 37107287533902102798797998220837590246510135740250
b = 46376937677490009712648124896970078050417018260538

c = a + b

print(f"c = {c}");

  # Constraints:
    # - JavaScript isn't able to handle the 50-digit numbers efficiently, but 
    #   Python IS able to handle them efficiently.
    # - Can the numbers in the given array be negative?
    #   - Yes.
    # - Can the numbers in the array be floating point numbers?
    #   - No. They must be integers.
    

# Devising a Plan
  # BRUTE FORCE SOLUTION
    # (1) Initialize a variable, "sum", with a value of 0, which will hold the 
    #     value of the running sum as the loop iterates through the given 
    #     array of numbers.
    # (2) Create a function, "findFirst10ofSum()", that takes in one parameter,
    #     an array of very large numbers, and returns one output, a 10-digit
    #     integer representing the first 10 digits of the very large sum of all
    #     the individual integers in the given array.
    # (3) Use a 'for' loop to iterate through the individual integers of the
    #     given array, adding each integer to the "sum" variable that we
    #     created in step (1).
    # (4) Return the value of "sum".
    
# Executing the Plan
# Reflect on/Iterate the Plan