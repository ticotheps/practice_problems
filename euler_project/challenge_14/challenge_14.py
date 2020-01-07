# UNDERSTANDING THE PROBLEM
  # - Objective: Find the "starting number" (that is LESS THAN 1,000,000) with
  #   the longest chain of numbers from "starting number" to "finishing number".
  
  # - Definitions:
    # - "starting number" = the first number, in a sequence of numbers, that
    #                     follow the 3 given rules of "Collatz Problem", which
    #                     are:
      # - Beginning with the "starting number", apply 1 of the following 3 rules  
      #   to that number to generate the next number in the sequence:
      #   (1) If the number, n, is even, perform 'n/2' to generate the next 
      #       number.
      #   (2) If the number, n, is odd, perform '3n + 1' to the generate the 
      #       next number.
      #   (3) If the number, n, is 1, stop evaluating numbers. This is the end of
      #       the sequence.
    
  # - Expected Inputs:
    # - Number of Expected Inputs: 1
    # - Name of Expected Input: "limitNumExclusive"
    # - Data Type of Expected Input: Integer
    
  # - Expected Outputs:
    # - Number of Expected Output: 1
    # - Name of Expected Output: "lenOfChain"
    # - Data Type of Expected Output: Integer
    
  # - Example Input:  4 (all positive integers BELOW this number are evaluated
  #                   for containing the longest chain)
  #   - 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
  #   - 2 -> 1
  #   - 1
  # - Example Output: 8 (3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
  

# DEVISING A PLAN


# EXECUTING THE PLAN


# REFLECTING ON/ITERATING THE PLAN