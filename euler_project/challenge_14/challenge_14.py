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
      
  # (2) Initialize a variable, 'currLongestChain', with a value of 0 to temporarily
      # hold the current highest n number of of integers in a chain while the
      # loop iterates through all numbers below the given input, 'limitNum'.
      
  # (3) Use a 'for' loop to iterate through all of the numbers between 1 and
      # 'limitNum', in descending fashion.
      
    # (4) Initialize a new variable, 'chainNums', with an empty array that 
        # will temporarily hold the values of chain numbers for each starting
        # number in our range.
      
    # (5) Initialize a new variable, 'currentChainNum', with the value of 
        # 'limitNum - 1'.
        
    # (6) Beginning with 'limitNum - 1', use a 'while' loop to generate the 
        # chain for each number BELOW the given 'limitNum' integer (exclusive),
        # in ascending order, using the given rules of Collatz sequence, 
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
  chainNumsArray = []
  currLongestChain = []
  # print("\nlongestChain = ", currLongestChain)
  startNumWithLongestChain = 0
  # print("startNumWithLongestChain = ", startNumWithLongestChain)
  nextChainNum = 0
  
  for i in range(1, limitNum):
    chainNumsForI = []
    # print("\nstartNum = ", i)
    currentChainNum = i
    # print("currentChainNum = ", currentChainNum)
    
    while currentChainNum >= 1:
      if (currentChainNum == 1):
        chainNumsForI.append(currentChainNum)
        # print("chainNumsForI = ", chainNumsForI)
        break
    
      # if 'currentChainNum' is an even number...
      if (currentChainNum % 2 == 0):
        chainNumsForI.append(currentChainNum)
        # print("chainNumsForI = ", chainNumsForI)
        nextChainNum = currentChainNum // 2
        # print("nextChainNum = ", nextChainNum)
        currentChainNum = nextChainNum
        # print("(even - AFTER) currentChainNum = ", currentChainNum)
        
      else:
        chainNumsForI.append(currentChainNum)
        # print("chainNumsForI = ", chainNumsForI)
        nextChainNum = (currentChainNum * 3) + 1
        # print("nextChainNum = ", nextChainNum)
        currentChainNum = nextChainNum
        # print("(odd - AFTER) currentChainNum = ", currentChainNum)
        
    chainNumsArray.append(chainNumsForI)
    
  for j in chainNumsArray:
    if (len(j) > len(currLongestChain)):
      currLongestChain = j
      # print("(AFTER) currLongestChain = ", currLongestChain)
      startNumWithLongestChain = j[0]
      # print("(AFTER) startNumWithLongestChain = ", startNumWithLongestChain)
      
  print("\ncurrLongestChain = ", currLongestChain)
  lenCurrLongest = len(currLongestChain)
  print("lenCurrLongest = ", lenCurrLongest)
  return startNumWithLongestChain

# Should print 3
print(f"The startNum with the longest chain (under 5) is {findLongestChainStartNum(5)}\n")

# Should print 9
print(f"The startNum with the longest chain (under 10) is {findLongestChainStartNum(10)}\n")


  

# REFLECTING ON/ITERATING THE PLAN