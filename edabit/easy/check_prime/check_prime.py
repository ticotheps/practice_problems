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
    is_prime = True
    
    if num > 1 and type(num) is int:
        num_of_divisors = 2
        
        for possible_divisor in range(2, num):

            if num_of_divisors > 2:
                is_prime = False 

                return is_prime
            else:
                if num % possible_divisor == 0:
                    num_of_divisors += 1
    else:
        is_prime = False

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