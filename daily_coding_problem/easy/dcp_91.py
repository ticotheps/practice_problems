# This problem was asked by Dropbox.

# What does the below code snippet print out?
# How can we fix he anonymous functions to behave as we'd expect?
# CODE SNIPPET:
# functions = []

# for i in range(10):
# 	functions.append(lambda : i)
  
# for f in functions:
#   print(f())

# UNDERSTAND:
#		- What is a 'lambda' (https://www.w3schools.com/python/python_lambda.asp)?
#			- A lambda function is a small anonymous function.
#			- A lambda function can take ANY number of arguments, but can only
#				have one expression.
#		- Lambda Syntax
#			- Lambda <arguments> : <expression>
#		- Process
#			- The expression is executed and the result is returned.
#     - Example #1 - A lambda function that adds 10 to the number passed in as an
#       argument, and print the result:

x = lambda a : a + 10
print(x(5))

#     - Example #2 - A lambda function that multiplies argument 'a' with
#       argument 'b' and prints the result:

y = lambda a, b : a * b
print(y(5, 6))
