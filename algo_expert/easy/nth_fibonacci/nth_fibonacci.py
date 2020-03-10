def getNthFib(n):
    # Declare the output variable to be returned.
    nthFibNum = 0
    
    # Initialize the list variable, with 0 and 1 (representing the 1st & 2nd
    # Fibonacci numbers in the sequence), for storing the fibonacci sequence.
    fibList = [0, 1]
    
    # Check to see if 'n' == 0 (Oth Fibonacci Number doesn't exist)
    if n == 0:
        return f"Sorry. Please pass an input value greater than 0."
    # Check to see if 'n' == 1 (1st Fibonacci Number is 0)
    elif n == 1:
        return 0
    # Check to see if 'n' == 2 (2nd Fibonacci Number is 1)
    elif n == 2:
        return 1
    # Check to see if 'n' >= 3
    else:
        # 3rd FibNum = 2nd Index of 'fibList'
        # 4th FibNum = 3rd Index of 'fibList'
        startFibIndex = 2
        for i in range(startFibIndex, n):
            twoNumsPrev = fibList[i - 2]
            oneNumPrev = fibList[i - 1]
            nextFibNum = twoNumsPrev + oneNumPrev
            fibList.append(nextFibNum)
            
        # Return the last index of the 'fibList' (nth Fibonacci number)
        nthFibNum = fibList[n - 1]
        return nthFibNum

print(getNthFib(2))  # should print 1
print(getNthFib(4))  # should print 2
print(getNthFib(6))  # should print 5


