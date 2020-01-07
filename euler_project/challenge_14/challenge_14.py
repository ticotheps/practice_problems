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
# - BRUTE FORCE SOLUTION
  # (1) Create a function, 'findLongestChainStartNum()', that takes in one
      # parameter, 'limitNum', & returns one output, 'longestChainStartNum'.
      
  # (2) Initialize a variable, 'longestChainStartNum', with a value of 0 to
      # hold the current startNum with the longest chain while the loop
      # iterates through all number below the given input, 'limitNum'.
      
  # (3) Use a 'for' loop to iterate through all of the numbers between 1 and
      # 'limitNum', in descending fashion.
      
    # (4) Initialize a new variable, 'chainNumsArray', with an empty array that 
        # will temporarily hold the values of chain numbers for each starting
        # number in our range.
      
    # (5) Initialize a new variable, 'currentChainNum', with the value of 
        # 'limitNum - 1'.
        
    # (6) Beginning with 'limitNum - 1', use a 'while' loop to generate the 
        # chain for each number BELOW the given 'limitNum' integer (exclusive),
        # in descending order, using the given rules of Collatz sequence, 
        # until'currentChainNum' is greater than 1.
        
      # (7) Find the length of the chain for that number.
      
      # (8) If the number is odd, perform '3n + 1' to generate the next number in
          # the sequence.
          
      # (9) If the number is even, perform 'n/2' to generate the next number in
          # the sequence.
          
      # (10) If the number is 1, stop.
      
    # (11) Return 'longestChainStartNum'.


# EXECUTING THE PLAN

def findLongestChainStartNum(limitNum):
  longestChainStartNum = 0
  nextChainNum = 
  
  for i in range(limitNum - 1, 0, -1):
    chainNumsArray = []
    print("i = ", i)
    currentChainNum = limitNum - 1
    print("currentChainNum = ", currentChainNum)
    
    if (currentChainNum == 1):
      return longestChainStartNum
    
    while currentChainNum > 1:
      # if 'currentChainNum' is an even number...
      if (currentChainNum % 2 == 0):
        nextChainNum = currentChainNum / 2
        
      else:
        next
        
  return longestChainStartNum

print(findLongestChainStartNum(5))
  

# REFLECTING ON/ITERATING THE PLAN