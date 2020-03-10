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
        return f"{fibList[0]}\n"
    # Check to see if 'n' == 2 (2nd Fibonacci Number is 1)
    elif n == 2:
        return f"{fibList[1]}\n"
    # Check to see if 'n' >= 3
    else:
        # 3rd FibNum = 2nd Index of 'fibList'
        # 4th FibNum = 3rd Index of 'fibList'
        startFibIndex = 2
        for i in range(startFibIndex, n):
            prev2ndNum = fibList[i - 2]
            print(f"prev2ndNum = {prev2ndNum}")
            
            prev1stNum = fibList[i - 1]
            print(f"prev1stNum = {prev1stNum}")
            
            nextFibNum = prev2ndNum + prev1stNum
            print(f"nextFibNum = {nextFibNum}")
            
            print("fibList_before =", fibList)
            fibList.append(nextFibNum)
            print("fibList_after =", fibList)
            
        # Return the last index of the 'fibList' (nth Fibonacci number)
        nthFibNum = fibList[-1]
        return f"nthFibNum = {nthFibNum}\n"

print(getNthFib(2))  # should print 1
print(getNthFib(4))  # should print 2
print(getNthFib(6))  # should print 5


