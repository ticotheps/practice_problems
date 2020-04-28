"""
CHECK IF A NUMBER IS PRIME

Objective:
    - Create a function that outputs True if a number is prime and False
        otherwise.
        
Examples:
    - check_prime(31) -> True
    - check_prime(18) -> False
    - check_prime(11) -> False
    
Notes:
    - A prime number has no other factors except 1 and itself.
    - 1 is NOT considered a prime number.
"""

"""
UNDERSTAND PHASE:
    
Defining Terms:
    - "prime":
    - A number greater than 1 that has no other positive divisors other than 1
        and itself.
        - i.e. - 2, 3, 5, 7, 11, etc.
        
Expected Inputs & Outputs:
    - Inputs:
        - Number of Inputs: 1
        - Input Type: integer
        - Input Name: 'num'
        
    - Outputs:
        - Number of Outputs: 1
        - Input Type: Boolean
        - Input Name: 'is_prime'  
        
Constraints:
    - Can the input be negative?
        - No.
    - Can the input be a floating point number?
        - No.
    - Can the input be 1?
        - No.
"""

# PLAN & EXECUTE PHASES:

def check_prime(num):
    # Declare a variable that designates the 'prime' status of 'num' input.
    # Initialize it with a value of True.
    is_prime = True
    
    # If input is valid (!= 1, positive, & whole integer), proceed with eval.
    if num > 1 and type(num) is int:
        print(f"\n{num} IS a valid input")
        
        # Declare a variable that keeps count of the number of divisors 
        #   that 'num' has. Initialize it with a value of 2, representing 
        #   the following divisors: 1, itself.
        num_of_divisors = 2
        print(f"(START) num_of_divisors for {num} = {num_of_divisors}")
        
        # Use a 'for' loop to iterate through a range of numbers that begin
        #   with '2' and end with 'num + 1' because '1' and 'num' have already
        #   been accounted for as divisors in the 'num_of_divisors' variable.
        for possible_divisor in range(2, num):
            # print(f"possible_divisor = {possible_divisor}")
            
            # Only continue evaluating if 'num_of_divisors' is not > 2.
            if num_of_divisors > 2:
                # If 'num_of_divisors' >2, change value of 'is_prime' to False.
                is_prime = False 
                
                # Return the value of 'is_prime' because no prime number has >2
                #   divisors.
                return is_prime
            # Otherwise, continue evaluating for other possible divisors for 'num'.
            else:
                # Check to see if 'num ' is evenly divisible by 'possible_divisor'.
                # If 'num' is evenly divisible by 'possible_divisor'...
                if num % possible_divisor == 0:
                    print(f"{num} IS evenly divisible by {possible_divisor}!")
                    
                    # ...add 1 to the value of 'num_of_divisors'.
                    num_of_divisors += 1   
                    print(f"(*STOP EVAL*) num_of_divisors for {num} = {num_of_divisors}") 
        
        print(f"(END) num_of_divisors = {num_of_divisors}") 
                      
    # If input is invalid, print a string saying input is invalid.
    else:
        print(f"\n{num} is NOT a valid input")
        # Change value of 'is_prime' to False.
        is_prime = False
        
    # Return the value of 'is_prime'
    return is_prime


print(check_prime(1)) # should print False  
print(check_prime(-31)) # should print False    
print(check_prime(-3.1)) # should print False
print(check_prime(3.1)) # should print False

print(check_prime(31)) # should print True
print(check_prime(18)) # should print False
print(check_prime(11)) # should print True

"""
REFLECT/REFACTOR PHASE:

Asymptotic Analysis:
    - Time Complexity: 
        - O(n) -> lineaer
    - Space Complexity:
        - O(1) -> constant
"""