# This problem was asked by Dropbox.

# What does the below code snippet print out?
# How can we fix he anonymous functions to behave as we'd expect?


# CODE SNIPPET:
# functions = []

# for i in range(10):
# 	functions.append(lambda : i)
  
# for f in functions:
#   print(f())

functions = []

for i in range(10):
	functions.append(i)
  
new_functions = list(map(lambda x: x, functions))
print(new_functions)

# for f in functions:
#   print(f())



# UNDERSTAND:
#		- What is a 'lambda' function? 
# 		- https://www.w3schools.com/python/python_lambda.asp
#			- A lambda function is a small anonymous function.
#			- A lambda function can take ANY number of arguments, but can only
#				have one expression.

#		- Lambda Syntax
#			- Lambda <arguments> : <expression>

#		- Lambda Procedure
#			- The expression is executed and the result is returned.

#		- Why use it?
#			- Use lambda functions when an anonymous function is required for a
#				short period of time.

#		- Examples
#   	- Example #1 - A lambda function that adds 10 to the number passed
#  			in as an argument, and print the result:

x = lambda a : a + 10
print(f"x = {x(5)}")

#     - Example #2 - A lambda function that multiplies argument 'a' with
#       argument 'b' and prints the result:

y = lambda a, b : a * b
print(f"y = {y(5, 6)}")

#     - Example #3 - A lambda function that sums arguments 'a', 'b', & 'c'
# 			and prints the result:

z = lambda a, b, c : a + b + c
print(f"z = {z(5, 6, 7)}")

#   	- Example #4 - The power of lambda is better shown when you use them
# 			as an anonymous function inside another function:
#				(a) You have a function definition ("myFunc()") that takes in ONE
# 					argument, & that argument will be multiplied with an unknown number.
#				(b)	Use that function definition to make a function that always doubles
#						the number you pass in as 'n':

def  myFunc(n):
  return lambda a : a * n

myDoubler = myFunc(2)
print(f"myDoubler(11) = {myDoubler(11)}")

#				(c)	Or use that SAME function definition to make a function that always
#						TRIPLES the number you pass in as 'n':

myTripler = myFunc(3)
print(f"myTripler(11) = {myTripler(11)}")

#		- CONCLUSION
# 		- Think of Lambda functions as "small, anonymous functions that
# 			allow you to interpolate something ('insert something of a different
# 			nature or value into something else') that is already being
#				interpolated".