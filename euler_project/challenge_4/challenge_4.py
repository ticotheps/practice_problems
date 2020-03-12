def check_palindrome(num):
    # Convert 'num' into a string & store in a var called 'numStr'.
    numStr = str(num)
    # print(f"numStr = {numStr}")
    
    # Split 'numStr' into a list of chars & store in a var called
    # 'numStrCharsList'.
    numStrCharsList = list(numStr)
    # print(f"numStrCharsList = {numStrCharsList}")
    
    # Reverse the order of the chars & store in a var called
    # 'revNumStrCharsList' using a 'backward step' in Python.
    revNumStrCharsList = numStrCharsList[::-1]
    # print(f"revNumStrCharsList = {revNumStrCharsList}")
    
    # Join all chars in 'revNumStrList' & store in a var called 'reversedNum'
    reversedNumStr = ''.join(revNumStrCharsList)
    # print(f"reversedNumStr = {reversedNumStr}")
    
    # Convert string back into an integer
    reversedNumStrInt = int(reversedNumStr)
    # print(f"reversedNumStrInt = {reversedNumStrInt}")
    
    # Determine if 'reversedNum' is equal to 'num'
    if num == reversedNumStrInt:
        # If it is, return True.
        # print("'num' IS a palindrome of 'reversedNumStrInt'")
        return True
    else:
        # If not, return False.
        # print("'num' is NOT a palindrome of 'reversedNumStrInt'")
        return False     

print(check_palindrome(12))  # should print False
print(check_palindrome(22))  # should print True
print(check_palindrome(22022))  # should print True


def find_largest_palindrome_product(n_digit_numbers):
    # Declare a var that will store the largest palindrome product to be returned
    largest_palindrome_product = 0
    # Declare a var that will store the single largest value in a digit to 9
    single_largest_digit_value = 9
    # Multiply the input by the single largest value in a digit to get the
    # maximum of your 'for' loop's range.
    startNumInt = int(str(single_largest_digit_value) * n_digit_numbers)
    print(f"startNumInt = {startNumInt}")
    
    # Iterate through all n-digit numbers
    for i in range(startNumInt, 0, -1):
        # Iterate through another list of n-digit numbers
        for j in range(startNumInt, 0, -1):
            product = i * j
            print(f"product = {product}")
            if check_palindrome(product) == True:
                if product > largest_palindrome_product:
                    largest_palindrome_product = product
                    print("We found the largest palindrome product!")
                    return largest_palindrome_product
    return "Sorry, there were no palindrome products found."
print(find_largest_palindrome_product(1))
print(find_largest_palindrome_product(2))
print(find_largest_palindrome_product(3))