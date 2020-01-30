# This problem was asked by Dropbox.

# What does the below code snippet print out?
# How can we fix he anonymous functions to behave as we'd expect?

functions = []

for i in range(10):
	functions.append(lambda : i)
  
for f in functions:
  print(f())


