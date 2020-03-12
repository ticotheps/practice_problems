def check_palindrome(num):
    # Convert 'num' into a string & store in a var called 'numStr'.
    numStr = str(num)
    print(f"numStr = {numStr}")
    
    # Split 'numStr' into a list of chars & store in a var called
    # 'numStrCharsList'.
    numStrCharsList = list(numStr)
    print(f"numStrCharsList = {numStrCharsList}")
    
    # Reverse the order of the chars & store in a var called
    # 'revNumStrCharsList' using a 'backward step' in Python.
    revNumStrCharsList = numStrCharsList[::-1]
    print(f"revNumStrCharsList = {revNumStrCharsList}")
    
    # Join all chars in 'revNumStrList' & store in a var called 'reversedNum'
    reversedNumStr = ''.join(revNumStrCharsList)
    print(f"reversedNumStr = {reversedNumStr}")
    
    # Convert string back into an integer
    reversedNumStrInt = int(reversedNumStr)
    print(f"reversedNumStrInt = {reversedNumStrInt}")
    
    # Determine if 'reversedNum' is equal to 'num'
    if num == reversedNumStrInt:
        # If it is, return True.
        print("'num' IS a palindrome of 'reversedNumStrInt'")
        return True
    else:
        # If not, return False.
        print("'num' is NOT a palindrome of 'reversedNumStrInt'")
        return False     

print(check_palindrome(12))  # should print False
print(check_palindrome(22))  # should print True
print(check_palindrome(22022))  # should print True


def find_largest_palindrome_product(num_of_digits):
    return num_of_digits

# print(find_largest_palindrome_product(1))
# print(find_largest_palindrome_product(2))
# print(find_largest_palindrome_product(3))