"""
ADD TWO STRING NUMBERS

Write a function that adds two numbers. The catch, however, is that the numbers
will be strings.

Examples:
    - add_str_nums("4", "5") -> "9"
    - add_str_nums("abcdefg", "3") -> "-1"
    - add_str_nums("1", "") -> "1"
    - add_str_nums("1874682736267235927359283579235789257", "32652983572985729")
   -> "1874682736267235927391936562808774986"
   
Notes:
    - If there are any non-numerical characters, return "-1".
    - If one option is blank, the code should still work.
    - Python supports the addiion of integers without limit, try this challenge
    without using this functionality.
    - Your function doesn't have to add negative numbers.
"""

"""
The U.P.E.R. Problem-Solving Framework

PHASE I: UNDERSTAND

- Objective: 
    - Write an algorithm that takes in two string inputs (each containing positive
      integers) and returns one output that is the sum of those positive
      integers.
      
- Expected Inputs:
    - Number Of: 2
    - Data Types: string, string
    - Var Names: 'num1', 'num2'
    
- Expected Outputs:
    - Number Of: 1
    - Data Type: string or integer
    - Var Name: 'sum'
    
- Edge Cases & Constraints:
    - Can the input strings be empty?
        - Yes. However, only ONE of the input strings can be empty. The other
          must contain an integer.
    - Can the input strings have negative numbers?
        - No. They must only contain positive whole numbers.
    - Can the input strings have floating point numbers?
        - No. They must only contain positive whole numbers.


PHASE II: PLAN

- Brute Force Solution:
    (1) Define a function that takes in two string inputs, 'num1' & 'num2', and
    returns a single output string (the sum of the positive integers inside of
    the input strings).
    
    (2) Evaluate both arguments to make sure that the contents of both strings
    are, in fact, positive whole numbers.
    
        (a) If they are both positive whole numbers, proceed.
        
        (b) If they are not BOTH positive whole numbers, return the string, '-1'.
        
    (3) Convert each argument from a string data type to a number data type.
    
    (4) Declare a new var, 'sum', that adds up the values of the converted
    string arguments together.
    
    (5) Convert the 'sum' var into a string data type and set it equal to a new
    var, 'sum_str'.
    
    (6) Return the value of 'sum_str'.
    
PHASE III: EXECUTE (Please See Below)
"""

def add_str_nums(num1, num2):
    # create a var, 'sum', to keep track of a running total sum
    sum = 0
    
    # evaluate both input strings to make sure that they are both positive
    # integers and are also not empty strings
    if type(num1) == str and type(num2) == str:
        # print(f"\nnum1 = {num1}")
        # print(f"num2 = {num2}")
        
        if num1 == "":
            print("num1 is an empty string")
        
        else:
            for i in num1:          
                if i.isnumeric() == True:
                    print(f"i = {i}, which is numeric")
                    
                else:
                    print(f"i = {i}, which is NOT numeric")
                    return "-1"
            sum += int(num1)
            # print(f"***UPDATED sum = {sum}")
                
        if num2 == "":
            print("num2 is an empty string")
        
        else:  
            for j in num2:
                if j.isnumeric() == True:
                    print(f"i = {j}, which is numeric")
                else:
                    print(f"i = {j}, which is NOT numeric")
                    return "-1"
            sum += int(num2)
            print(f"***UPDATED sum = {sum}")

        return str(sum)
    
    else:
        return "The provided inputs are both not of string data type. Please enter a valid input."
        

print(add_str_nums("", ""))  # "0"
print(add_str_nums("1", "01"))  # "2"
print(add_str_nums("1", ""))  # "1"
print(add_str_nums("198547982570192857109283570192837509218375091283750192835710298357019237509125710925710923759012375901275901285701925712035712983571092562945875310962518235712385971230956127856123571209358712905610923587102395716258125612095710298","510298570192857910827519027510982561875691857120958371029586187585198273501982573091857091875901875809175091659812750918275091875091857918265901265918659816591750981750981759817598175089175891720570129571098758901750917501975"))  #   "198548492868763049967194397711865020200936966975607313794081327943206822707399212908284015616104251803151710460793585524786631258662967654803793576863784154372202562981937878837883388807533802081502644157231966815017027363013212273"
print(add_str_nums("0000001", "020006"))  # "20007"
print(add_str_nums("1325123515s238579875987", "38698592523525325"))  # "-1"


"""
PHASE IV: REFLECT/REFACTOR

- FIRST-PASS SOLUTION:
    - Asymptotic Analysis:
        - Time Complexity: O(n) -> "linear"
        - Space Complexity: O(1) -> "constant"
"""